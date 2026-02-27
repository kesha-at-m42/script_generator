"""
Reusable JSON editor component for Streamlit.

Supports view mode (st.json collapsible tree) and edit mode (st.text_area)
toggled by a button.
"""

import json
from typing import Callable, Optional

import streamlit as st


def render_json_editor(
    data: dict,
    key: str,
    read_only: bool = False,
    height: int = 500,
    on_save: Optional[Callable[[dict], None]] = None,
    save_label: str = "💾 Save",
) -> Optional[dict]:
    """
    Render a JSON viewer/editor with view/edit toggle.

    View mode: interactive collapsible tree via st.json()
    Edit mode: raw JSON text area with live validation feedback

    Args:
        data: The dict to display/edit.
        key: Unique key prefix for all Streamlit widgets in this component.
        read_only: If True, only show view mode with no edit toggle.
        height: Height in pixels of the text area in edit mode.
        on_save: Callback called with the parsed dict on successful save.
                 If None, saving just exits edit mode.
        save_label: Label for the save button.

    Returns:
        The current parsed dict (from edit buffer if in edit mode, else the
        original data), or None if the edit buffer contains invalid JSON.
    """
    edit_mode_key = f"__json_edit_mode_{key}"
    edit_text_key = f"__json_edit_text_{key}"

    # Normalise input: accept JSON string as well as dict
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except json.JSONDecodeError as exc:
            st.error(f"render_json_editor: invalid JSON string — {exc}")
            return None

    # Initialise session state on first render
    if edit_mode_key not in st.session_state:
        st.session_state[edit_mode_key] = False
    if edit_text_key not in st.session_state:
        st.session_state[edit_text_key] = json.dumps(data, indent=2)

    is_editing: bool = st.session_state[edit_mode_key]

    # ── Toggle button row ────────────────────────────────────────────────────
    if not read_only:
        col_btn, _ = st.columns([1, 7])
        with col_btn:
            if is_editing:
                if st.button("👁 View", key=f"{key}__toggle"):
                    st.session_state[edit_mode_key] = False
                    st.rerun()
            else:
                if st.button("✏️ Edit", key=f"{key}__toggle"):
                    # Sync buffer to current data before entering edit mode
                    st.session_state[edit_text_key] = json.dumps(data, indent=2)
                    st.session_state[edit_mode_key] = True
                    st.rerun()

    # ── Edit mode ────────────────────────────────────────────────────────────
    if is_editing and not read_only:
        edited_text = st.text_area(
            "JSON editor",
            value=st.session_state[edit_text_key],
            height=height,
            key=f"{key}__textarea",
            label_visibility="collapsed",
        )
        # Keep buffer in sync across reruns
        st.session_state[edit_text_key] = edited_text

        # Live validation
        parsed: Optional[dict] = None
        try:
            parsed = json.loads(edited_text)
            st.caption("✅ Valid JSON")
        except json.JSONDecodeError as exc:
            st.error(f"Invalid JSON: {exc}")

        # Save button
        if st.button(save_label, key=f"{key}__save", disabled=(parsed is None)):
            if on_save is not None:
                try:
                    on_save(parsed)
                    st.success("Saved.")
                    st.session_state[edit_mode_key] = False
                    st.rerun()
                except Exception as exc:
                    st.error(f"Save failed: {exc}")
            else:
                st.session_state[edit_mode_key] = False
                st.rerun()

        return parsed

    # ── View mode ────────────────────────────────────────────────────────────
    else:
        st.json(data)
        return data
