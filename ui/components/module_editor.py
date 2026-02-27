"""
Designer/writer-friendly module starter pack editor.

Renders a module JSON as a structured form (text inputs, text areas,
editable tables) instead of a raw JSON text area.
"""

from __future__ import annotations

from typing import Callable, Optional

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

_PHASE_NAMES = ["warm_up", "lesson", "practice", "assessment", "review"]


def _df_from_strings(items: list, col: str) -> pd.DataFrame:
    return pd.DataFrame({col: [str(i) for i in (items or [])]})


def _strings_from_df(df: pd.DataFrame, col: str) -> list[str]:
    return [str(v) for v in df[col].dropna() if str(v).strip()]


def _vocab_intro_to_df(items: list) -> pd.DataFrame:
    """Normalise vocabulary_introduced_in_order to a word/definition table."""
    rows = []
    for item in items or []:
        if isinstance(item, str):
            rows.append({"word": item, "definition": ""})
        elif isinstance(item, dict):
            for word, defn in item.items():
                rows.append({"word": word, "definition": str(defn) if defn else ""})
    return pd.DataFrame(rows) if rows else pd.DataFrame(columns=["word", "definition"])


def _df_to_vocab_intro(df: pd.DataFrame) -> list:
    """Convert word/definition table back to the original mixed-format list."""
    result = []
    for _, row in df.iterrows():
        word = str(row.get("word", "")).strip()
        defn = str(row.get("definition", "")).strip()
        if not word:
            continue
        if defn:
            result.append({word: defn})
        else:
            result.append(word)
    return result


def _misconceptions_to_df(items: list) -> pd.DataFrame:
    rows = [
        {
            "title": m.get("misconception", ""),
            "description": m.get("description", ""),
        }
        for m in (items or [])
    ]
    return pd.DataFrame(rows) if rows else pd.DataFrame(columns=["title", "description"])


def _df_to_misconceptions(df: pd.DataFrame, original: list) -> list:
    result = []
    for i, row in df.iterrows():
        title = str(row.get("title", "")).strip()
        description = str(row.get("description", "")).strip()
        if not title and not description:
            continue
        # preserve original id if available
        orig_id = str(original[i]["id"]) if i < len(original) else str(i + 1)
        result.append({"id": orig_id, "misconception": title, "description": description})
    return result


# ---------------------------------------------------------------------------
# Public component
# ---------------------------------------------------------------------------


def render_module_editor(
    data: dict,
    key: str,
    on_save: Optional[Callable[[dict], None]] = None,
) -> None:
    """Render a designer/writer-friendly form for a module starter pack.

    All fields are shown as labeled inputs or editable tables. A single
    "Save Module" button at the bottom calls *on_save* with the collected dict.

    Args:
        data:    The current module dict (loaded from JSON).
        key:     Unique key prefix for Streamlit widgets.
        on_save: Callback receiving the updated dict on successful save.
    """
    with st.form(key=f"{key}__form"):
        # ── Basic info ───────────────────────────────────────────────────────
        st.subheader("Basic Info")
        col_name, col_grade = st.columns([3, 1])
        with col_name:
            module_name = st.text_input(
                "Module name",
                value=data.get("module_name", ""),
                key=f"{key}__module_name",
            )
        with col_grade:
            grade_level = st.number_input(
                "Grade level",
                value=int(data.get("grade_level", 1)),
                min_value=1,
                max_value=12,
                step=1,
                key=f"{key}__grade_level",
            )

        st.divider()

        # ── Learning goals ───────────────────────────────────────────────────
        st.subheader("Learning Goals")
        st.caption("One goal per row. Use the ＋ icon in the table to add rows.")
        goals_df = _df_from_strings(data.get("learning_goals", []), "learning_goal")
        goals_edited = st.data_editor(
            goals_df,
            num_rows="dynamic",
            use_container_width=True,
            key=f"{key}__goals",
            column_config={
                "learning_goal": st.column_config.TextColumn("Learning Goal", width="large")
            },
        )

        st.divider()

        # ── Vocabulary ───────────────────────────────────────────────────────
        st.subheader("Vocabulary")
        st.caption("All words available in this module.")
        vocab_df = _df_from_strings(data.get("vocabulary", []), "word")
        vocab_edited = st.data_editor(
            vocab_df,
            num_rows="dynamic",
            use_container_width=True,
            key=f"{key}__vocab",
            column_config={"word": st.column_config.TextColumn("Word", width="medium")},
        )

        st.divider()

        # ── Core concepts ────────────────────────────────────────────────────
        core = data.get("core_concepts")
        if core is not None:
            st.subheader("Core Concepts")
            core_df = _df_from_strings(core, "concept")
            core_edited = st.data_editor(
                core_df,
                num_rows="dynamic",
                use_container_width=True,
                key=f"{key}__core",
                column_config={"concept": st.column_config.TextColumn("Concept", width="medium")},
            )
            st.divider()
        else:
            core_edited = None

        # ── Standards ────────────────────────────────────────────────────────
        standards = data.get("standards")
        if standards is not None:
            st.subheader("Standards")
            std_col1, std_col2, std_col3 = st.columns(3)
            with std_col1:
                st.caption("Building on")
                std_on_df = _df_from_strings(standards.get("building_on", []), "standard")
                std_on_edited = st.data_editor(
                    std_on_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__std_on",
                )
            with std_col2:
                st.caption("Addressing")
                std_addr_df = _df_from_strings(standards.get("addressing", []), "standard")
                std_addr_edited = st.data_editor(
                    std_addr_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__std_addr",
                )
            with std_col3:
                st.caption("Building toward")
                std_toward_df = _df_from_strings(standards.get("building_toward", []), "standard")
                std_toward_edited = st.data_editor(
                    std_toward_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__std_toward",
                )
            st.divider()
        else:
            std_on_edited = std_addr_edited = std_toward_edited = None

        # ── Available visuals ────────────────────────────────────────────────
        visuals = data.get("available_visuals")
        if visuals is not None:
            st.subheader("Available Visuals")
            vis_desc = st.text_area(
                "Description",
                value=visuals.get("description", ""),
                height=80,
                key=f"{key}__vis_desc",
            )
            vis_col1, vis_col2 = st.columns(2)
            with vis_col1:
                st.caption("Tangibles")
                vis_tang_df = _df_from_strings(visuals.get("tangibles", []), "tangible")
                vis_tang_edited = st.data_editor(
                    vis_tang_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__vis_tang",
                )
            with vis_col2:
                st.caption("Constraints")
                vis_con_df = _df_from_strings(visuals.get("constraints", []), "constraint")
                vis_con_edited = st.data_editor(
                    vis_con_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__vis_con",
                )
            st.divider()
        else:
            vis_desc = vis_tang_edited = vis_con_edited = None

        # ── Scope fence ──────────────────────────────────────────────────────
        scope = data.get("scope_fence")
        if scope is not None:
            st.subheader("Scope Fence")
            st.caption("Topics and vocabulary NOT covered in this module.")
            sf_col1, sf_col2 = st.columns(2)
            with sf_col1:
                st.caption("Don't use vocabulary")
                sf_vocab_df = _df_from_strings(scope.get("advanced_vocabulary", []), "word")
                sf_vocab_edited = st.data_editor(
                    sf_vocab_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__sf_vocab",
                )
            with sf_col2:
                st.caption("Don't cover concepts")
                sf_con_df = _df_from_strings(scope.get("advanced_concepts", []), "concept")
                sf_con_edited = st.data_editor(
                    sf_con_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__sf_con",
                )
            st.divider()
        else:
            sf_vocab_edited = sf_con_edited = None

        # ── Misconceptions ───────────────────────────────────────────────────
        misconceptions = data.get("misconceptions")
        if misconceptions is not None:
            st.subheader("Misconceptions")
            misc_df = _misconceptions_to_df(misconceptions)
            misc_edited = st.data_editor(
                misc_df,
                num_rows="dynamic",
                use_container_width=True,
                key=f"{key}__misc",
                column_config={
                    "title": st.column_config.TextColumn("Misconception", width="medium"),
                    "description": st.column_config.TextColumn("Description", width="large"),
                },
            )
            st.divider()
        else:
            misc_edited = None

        # ── Phases ───────────────────────────────────────────────────────────
        phases = data.get("phases")
        phases_out: list[dict] = []
        if phases is not None:
            st.subheader("Phases")
            for p_idx, phase in enumerate(phases):
                p_name = phase.get("phase_name", f"Phase {p_idx + 1}")
                st.markdown(f"**Phase {p_idx + 1}: {p_name}**")

                p_col1, p_col2 = st.columns([3, 1])
                with p_col1:
                    p_name_val = st.text_input(
                        "Phase name",
                        value=p_name,
                        key=f"{key}__p{p_idx}_name",
                    )
                with p_col2:
                    p_interactions = st.text_input(
                        "Interaction count",
                        value=phase.get("interaction_count", ""),
                        help='e.g. "2-3" or "6-8"',
                        key=f"{key}__p{p_idx}_interactions",
                    )

                p_purpose = st.text_area(
                    "Purpose",
                    value=phase.get("purpose", ""),
                    height=80,
                    key=f"{key}__p{p_idx}_purpose",
                )

                st.caption("Vocabulary introduced in order (leave definition blank if none)")
                vocab_intro_df = _vocab_intro_to_df(phase.get("vocabulary_introduced_in_order", []))
                vocab_intro_edited = st.data_editor(
                    vocab_intro_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__p{p_idx}_vocab_intro",
                    column_config={
                        "word": st.column_config.TextColumn("Word", width="small"),
                        "definition": st.column_config.TextColumn(
                            "Definition (optional)", width="large"
                        ),
                    },
                )

                phases_out.append(
                    {
                        **phase,  # preserve any fields we don't render (e.g. variables)
                        "phase_name": p_name_val,
                        "interaction_count": p_interactions,
                        "purpose": p_purpose,
                        "vocabulary_introduced_in_order": "_PLACEHOLDER_",
                        "__vocab_intro_df": vocab_intro_edited,
                    }
                )

                if p_idx < len(phases) - 1:
                    st.markdown("---")

            st.divider()

        # ── Top-level variables ──────────────────────────────────────────────
        top_vars = data.get("variables")
        vars_dfs: dict[str, pd.DataFrame] = {}
        if top_vars is not None:
            st.subheader("Variables")
            st.caption("Lists used by prompt templates.")
            for var_key, var_vals in top_vars.items():
                st.caption(var_key)
                v_df = _df_from_strings(var_vals if isinstance(var_vals, list) else [], var_key)
                vars_dfs[var_key] = st.data_editor(
                    v_df,
                    num_rows="dynamic",
                    use_container_width=True,
                    key=f"{key}__var_{var_key}",
                )
            st.divider()

        # ── Save ─────────────────────────────────────────────────────────────
        submitted = st.form_submit_button("💾 Save Module", use_container_width=True)

    # ── Collect + persist (outside the form) ────────────────────────────────
    if submitted:
        new_data: dict = dict(data)  # start from original to preserve unknown fields

        new_data["module_name"] = module_name
        new_data["grade_level"] = int(grade_level)

        if "module_number" in data:
            new_data["module_number"] = data["module_number"]

        new_data["learning_goals"] = _strings_from_df(goals_edited, "learning_goal")
        new_data["vocabulary"] = _strings_from_df(vocab_edited, "word")

        if core_edited is not None:
            new_data["core_concepts"] = _strings_from_df(core_edited, "concept")

        if standards is not None:
            new_data["standards"] = {
                "building_on": _strings_from_df(std_on_edited, "standard"),
                "addressing": _strings_from_df(std_addr_edited, "standard"),
                "building_toward": _strings_from_df(std_toward_edited, "standard"),
            }

        if visuals is not None:
            new_data["available_visuals"] = {
                **visuals,
                "description": vis_desc,
                "tangibles": _strings_from_df(vis_tang_edited, "tangible"),
                "constraints": _strings_from_df(vis_con_edited, "constraint"),
            }

        if scope is not None:
            new_data["scope_fence"] = {
                "advanced_vocabulary": _strings_from_df(sf_vocab_edited, "word"),
                "advanced_concepts": _strings_from_df(sf_con_edited, "concept"),
            }

        if misconceptions is not None:
            new_data["misconceptions"] = _df_to_misconceptions(misc_edited, misconceptions)

        if phases is not None:
            rebuilt_phases = []
            for p in phases_out:
                vocab_intro_df = p.pop("__vocab_intro_df")
                p["vocabulary_introduced_in_order"] = _df_to_vocab_intro(vocab_intro_df)
                rebuilt_phases.append(p)
            new_data["phases"] = rebuilt_phases

        if top_vars is not None:
            new_data["variables"] = {k: _strings_from_df(v_df, k) for k, v_df in vars_dfs.items()}

        if on_save is not None:
            try:
                on_save(new_data)
                st.success("Module saved.")
            except Exception as exc:
                st.error(f"Save failed: {exc}")
