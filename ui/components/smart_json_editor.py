"""
Generic recursive JSON editor for Streamlit.

Adapts its widgets to the data shape at each level:

  str / int / float / bool / None  → appropriate input widget
  list[scalar]                     → single-column st.data_editor
  list[{"key": "value"} items]     → term/definition st.data_editor
  list[uniform flat dict]          → multi-column st.data_editor
  list[complex object]             → per-item expander (recursive)
  dict                             → labeled fields / expander (recursive)
  any node deeper than _MAX_DEPTH  → raw JSON text area

A "Raw JSON" toggle falls back to the plain text-area editor for anything
the smart form cannot represent cleanly.
"""

from __future__ import annotations

import json
from typing import Any, Callable, Optional, Union

import pandas as pd
import streamlit as st

from ui.components.json_editor import render_json_editor

# Nodes nested deeper than this render as raw JSON text areas.
_MAX_DEPTH = 3


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _fmt(key: str) -> str:
    """Format a dict key as a readable label. Preserves leading sigils (@, $)."""
    if key and key[0] in ("@", "$", "#"):
        return key
    return key.replace("_", " ").capitalize()


def _wkey(path: str) -> str:
    """Turn a dot-path into a safe Streamlit widget key."""
    return (
        path.replace(".", "__")
        .replace("[", "__")
        .replace("]", "__")
        .replace(" ", "_")
        .replace("@", "at_")
        .replace("$", "dollar_")
    )


# ---------------------------------------------------------------------------
# List classification
# ---------------------------------------------------------------------------


def _classify(items: list) -> str:
    """Classify a non-empty list for rendering purposes.

    Returns one of:
        "empty"                – len == 0
        "scalar"               – all items are str/int/float/bool/None
        "single_key_dicts"     – each item is a one-key dict (term→definition)
        "uniform_flat_dicts"   – all items are dicts with identical keys, all scalar values
        "uniform_complex_dicts"– all items are dicts with identical keys, some non-scalar values
        "nonuniform_dicts"     – dicts with different key sets
        "mixed"                – anything else
    """
    if not items:
        return "empty"

    if all(isinstance(i, (str, int, float, bool)) or i is None for i in items):
        return "scalar"

    if not all(isinstance(i, dict) for i in items):
        return "mixed"

    # All dicts ────────────────────────────────────────────────────────────
    if all(len(d) == 1 for d in items):
        return "single_key_dicts"

    key_sets = [frozenset(d.keys()) for d in items]
    if len(set(key_sets)) > 1:
        return "nonuniform_dicts"

    # Uniform key sets — flat or complex?
    all_flat = all(
        isinstance(v, (str, int, float, bool)) or v is None for d in items for v in d.values()
    )
    return "uniform_flat_dicts" if all_flat else "uniform_complex_dicts"


# ---------------------------------------------------------------------------
# DataFrame helpers
# ---------------------------------------------------------------------------


def _scalars_to_df(items: list, col: str) -> pd.DataFrame:
    return pd.DataFrame({col: [("" if v is None else str(v)) for v in items]})


def _df_to_scalars(df: pd.DataFrame, col: str, orig_type: type) -> list:
    result = []
    for raw in df[col].dropna():
        s = str(raw).strip()
        if not s:
            continue
        if orig_type is int:
            try:
                result.append(int(float(s)))
                continue
            except (ValueError, TypeError):
                pass
        if orig_type is float:
            try:
                result.append(float(s))
                continue
            except (ValueError, TypeError):
                pass
        result.append(s)
    return result


def _item_label(item: dict, index: int) -> str:
    """Pick a short human-readable title for a complex list item."""
    for hint in (
        "phase_name",
        "name",
        "title",
        "misconception",
        "label",
        "problem_instance_id",
        "id",
    ):
        val = item.get(hint)
        if val is not None and isinstance(val, (str, int)) and str(val).strip():
            return f"[{index}] {val}"
    return f"Item {index + 1}"


# ---------------------------------------------------------------------------
# Core recursive renderer
# Must be called inside a st.form context.
# ---------------------------------------------------------------------------


def _node(value: Any, path: str, depth: int, label: Optional[str]) -> Any:
    """Render one JSON node and return the (possibly edited) value."""
    k = _wkey(path)
    lv = "visible" if label else "collapsed"

    # ── bool (before int, since bool is a subclass of int) ──────────────────
    if isinstance(value, bool):
        return st.checkbox(label or "", value=value, key=k)

    # ── int ──────────────────────────────────────────────────────────────────
    if isinstance(value, int):
        return int(st.number_input(label or "", value=value, step=1, key=k, label_visibility=lv))

    # ── float ────────────────────────────────────────────────────────────────
    if isinstance(value, float):
        return float(st.number_input(label or "", value=value, key=k, label_visibility=lv))

    # ── None ─────────────────────────────────────────────────────────────────
    if value is None:
        st.caption(f"{label}: —" if label else "—")
        return None

    # ── str ──────────────────────────────────────────────────────────────────
    if isinstance(value, str):
        if len(value) > 100 or "\n" in value:
            return st.text_area(label or "", value=value, height=100, key=k, label_visibility=lv)
        return st.text_input(label or "", value=value, key=k, label_visibility=lv)

    # ── dict ─────────────────────────────────────────────────────────────────
    if isinstance(value, dict):
        if depth >= _MAX_DEPTH:
            raw = st.text_area(
                (label + " (raw JSON)") if label else "raw JSON",
                value=json.dumps(value, indent=2),
                height=120,
                key=k,
                label_visibility=lv,
            )
            try:
                return json.loads(raw)
            except json.JSONDecodeError:
                return value

        def _dict_body() -> dict:
            result: dict = {}
            for dk, dv in value.items():
                result[dk] = _node(dv, f"{path}.{dk}", depth + 1, _fmt(dk))
            return result

        if label:
            with st.expander(_fmt(label), expanded=(depth <= 1)):
                return _dict_body()
        else:
            return _dict_body()

    # ── list ─────────────────────────────────────────────────────────────────
    if isinstance(value, list):
        return _list(value, path, depth, label)

    # ── unknown type – raw JSON fallback ─────────────────────────────────────
    raw = st.text_area(label or "", value=json.dumps(value, indent=2), key=k, label_visibility=lv)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return value


def _list(items: list, path: str, depth: int, label: Optional[str]) -> list:
    """Render a list using the most appropriate widget."""
    k = _wkey(path)
    kind = _classify(items)

    if label:
        st.markdown(f"**{_fmt(label)}**")

    # ── Empty ────────────────────────────────────────────────────────────────
    if kind == "empty":
        df = pd.DataFrame({"value": pd.Series([], dtype=str)})
        edited = st.data_editor(df, num_rows="dynamic", use_container_width=True, key=k)
        return [v for v in edited["value"].dropna() if str(v).strip()]

    # ── Scalars → single-column table ────────────────────────────────────────
    if kind == "scalar":
        col = label or "value"
        orig_type = type(next((v for v in items if v is not None), ""))
        df = _scalars_to_df(items, col)
        cfg = {col: st.column_config.TextColumn(_fmt(col), width="stretch")}
        edited = st.data_editor(
            df, num_rows="dynamic", use_container_width=True, key=k, column_config=cfg
        )
        return _df_to_scalars(edited, col, orig_type)

    # ── Single-key dicts → term/definition table ─────────────────────────────
    if kind == "single_key_dicts":
        rows = [
            {"term": list(d.keys())[0], "definition": str(list(d.values())[0] or "")} for d in items
        ]
        df = pd.DataFrame(rows)
        edited = st.data_editor(
            df,
            num_rows="dynamic",
            use_container_width=True,
            key=k,
            column_config={
                "term": st.column_config.TextColumn("Term", width="small"),
                "definition": st.column_config.TextColumn("Definition", width="large"),
            },
        )
        return [
            {str(r["term"]).strip(): str(r.get("definition", "")).strip()}
            for _, r in edited.iterrows()
            if str(r.get("term", "")).strip()
        ]

    # ── Uniform flat dicts → spreadsheet ─────────────────────────────────────
    if kind == "uniform_flat_dicts":
        df = pd.DataFrame(items)
        cfg = {}
        for c in df.columns:
            # Infer column config from the first non-None value in this column
            sample = next((item[c] for item in items if c in item and item[c] is not None), None)
            if isinstance(sample, bool):
                cfg[c] = st.column_config.CheckboxColumn(_fmt(c))
            elif isinstance(sample, int):
                cfg[c] = st.column_config.NumberColumn(_fmt(c), format="%d", step=1)
            elif isinstance(sample, float):
                cfg[c] = st.column_config.NumberColumn(_fmt(c))
            else:
                cfg[c] = st.column_config.TextColumn(_fmt(c))
        edited = st.data_editor(
            df, num_rows="dynamic", use_container_width=True, key=k, column_config=cfg
        )
        records = edited.dropna(how="all").to_dict("records")
        return [r for r in records if any(str(v).strip() for v in r.values())]

    # ── Uniform complex dicts → per-item expanders ────────────────────────────
    if kind == "uniform_complex_dicts":
        result = []
        for i, item in enumerate(items):
            with st.expander(_item_label(item, i), expanded=False):
                r: dict = {}
                for dk, dv in item.items():
                    r[dk] = _node(dv, f"{path}.{i}.{dk}", depth + 1, _fmt(dk))
                result.append(r)
        st.caption(f"ℹ️ {len(items)} item(s) — to add or remove items, use Raw JSON.")
        return result

    # ── Fallback: raw JSON text area ─────────────────────────────────────────
    raw = st.text_area(
        "items (raw JSON)",
        value=json.dumps(items, indent=2),
        key=k,
        label_visibility="collapsed",
    )
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return items


# ---------------------------------------------------------------------------
# Markdown read view
# ---------------------------------------------------------------------------

_TEXT_TYPES = (str, int, float, bool)


def _render_markdown_view(data: Any, visible_fields: Optional[list] = None) -> None:
    """Render JSON as clean readable prose — no form widgets.

    Useful for reviewing dialogue/prompt text without editor noise.
    Only string and scalar fields are shown; nested structures are skipped.
    """
    if isinstance(data, list):
        for i, item in enumerate(data):
            if not isinstance(item, dict):
                st.markdown(f"- {item}")
                continue
            label = _item_label(item, i)
            st.markdown(f"#### {label}")
            fields = visible_fields if visible_fields else list(item.keys())
            for field in fields:
                if field not in item:
                    continue
                val = item[field]
                if not isinstance(val, _TEXT_TYPES):
                    continue
                display = _fmt(field)
                if isinstance(val, str) and len(val) > 80:
                    st.markdown(f"**{display}**")
                    st.markdown(val)
                else:
                    st.markdown(f"**{display}:** {val}")
            st.divider()
    elif isinstance(data, dict):
        fields = visible_fields if visible_fields else list(data.keys())
        for field in fields:
            if field not in data:
                continue
            val = data[field]
            if not isinstance(val, _TEXT_TYPES):
                continue
            display = _fmt(field)
            if isinstance(val, str) and len(val) > 80:
                st.markdown(f"**{display}**")
                st.markdown(val)
            else:
                st.markdown(f"**{display}:** {val}")
    else:
        st.markdown(str(data))


# ---------------------------------------------------------------------------
# Public component
# ---------------------------------------------------------------------------


def render_smart_json_editor(
    data: Union[dict, list],
    key: str,
    read_only: bool = False,
    height: int = 500,
    on_save: Optional[Callable[[Any], None]] = None,
    save_label: str = "💾 Save",
) -> None:
    """Render a smart JSON editor that adapts its widgets to the data shape.

    Works for any JSON structure without schema knowledge. New fields in the
    JSON are picked up automatically on the next render.

    Args:
        data:       The JSON value to display/edit (dict or list).
        key:        Unique widget-key prefix (must be unique across the page).
        read_only:  If True, render a non-editable collapsible tree.
        height:     Height in pixels of the raw JSON text area (fallback mode).
        on_save:    Callback receiving the updated value when the form is saved.
        save_label: Label for the save button.
    """
    if read_only:
        st.json(data)
        return

    # ── View mode selector ────────────────────────────────────────────────────
    mode: str = st.radio(
        "View mode",
        options=["Form", "Raw JSON", "Read"],
        horizontal=True,
        key=f"{key}__mode",
        label_visibility="collapsed",
    )

    if mode == "Raw JSON":
        render_json_editor(data, key=f"{key}__raw", read_only=False, height=height, on_save=on_save)
        return

    # ── Field checklist for arrays of objects (outside form) ─────────────────
    # Detected for top-level lists of dicts; lets writers omit technical fields
    # while preserving them invisibly so saves never drop data.
    hidden_fields: list[str] = []
    display_data: Any = data
    visible: list[str] = []

    if (
        isinstance(data, list)
        and data
        and _classify(data) in ("uniform_flat_dicts", "uniform_complex_dicts")
    ):
        all_fields = list(data[0].keys())

        # Infer a schema hint from the @type field if present
        type_hint = data[0].get("@type")
        schema_label = f"{len(data)} items"
        if isinstance(type_hint, str):
            schema_label += f" ({type_hint})"
        schema_label += f" · {len(all_fields)} fields"

        with st.expander(f"🔍 Fields  —  {schema_label}", expanded=False):
            st.caption("Hidden fields are preserved on save.")
            n_cols = min(len(all_fields), 4)
            rows = [all_fields[i : i + n_cols] for i in range(0, len(all_fields), n_cols)]
            for row_fields in rows:
                cols = st.columns(n_cols)
                for j, field in enumerate(row_fields):
                    cb_key = f"{key}__field_{field}"
                    if cb_key not in st.session_state:
                        st.session_state[cb_key] = True  # visible by default
                    with cols[j]:
                        if st.checkbox(field, key=cb_key):
                            visible.append(field)

        if not visible:
            visible = all_fields  # guard: never show nothing

        hidden_fields = [f for f in all_fields if f not in visible]
        if hidden_fields:
            display_data = [{k: v for k, v in item.items() if k in visible} for item in data]

    # ── Read (markdown) mode ──────────────────────────────────────────────────
    if mode == "Read":
        _render_markdown_view(display_data, visible_fields=visible or None)
        return

    # ── Smart form (edit) mode ────────────────────────────────────────────────
    with st.form(key=f"{key}__form"):
        result = _node(display_data, path=key, depth=0, label=None)
        submitted = st.form_submit_button(save_label, use_container_width=True)

    if submitted and on_save is not None:
        try:
            # Re-attach hidden fields from the original data so they are not lost
            if hidden_fields and isinstance(result, list):
                for i, new_item in enumerate(result):
                    if i < len(data) and isinstance(data[i], dict):
                        for hf in hidden_fields:
                            if hf in data[i]:
                                new_item[hf] = data[i][hf]
            on_save(result)
            st.success("Saved.")
        except Exception as exc:
            st.error(f"Save failed: {exc}")
