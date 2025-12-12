"""
Centralized output handling utilities for both interactive and non-interactive modes.
"""

import io
import json
import contextlib
import sys
from pathlib import Path
from typing import Optional, Any, List, Dict
import streamlit as st


class StreamingConsoleCapture(io.StringIO):
    """
    Custom StringIO that captures output AND displays it in real-time to Streamlit.
    """
    def __init__(self, display_container):
        super().__init__()
        self.display_container = display_container
        self.lines = []

    def write(self, text):
        # Write to buffer
        result = super().write(text)

        # Also update the display in real-time
        if text and text.strip():
            self.lines.append(text)
            # Update the display container with all accumulated output
            full_output = ''.join(self.lines)
            self.display_container.code(full_output, language="log")

        return result


@contextlib.contextmanager
def capture_console_output_streaming(console_placeholder=None):
    """
    Context manager that captures stdout AND displays it in real-time.

    Usage:
        console_display = st.empty()
        with capture_console_output_streaming(console_display) as buffer:
            print("This will be captured AND displayed in real-time")
        full_output = buffer.getvalue()

    Args:
        console_placeholder: Streamlit empty container to display output in real-time

    Yields:
        StreamingConsoleCapture: Buffer containing captured output
    """
    if console_placeholder is not None:
        buffer = StreamingConsoleCapture(console_placeholder)
    else:
        buffer = io.StringIO()

    with contextlib.redirect_stdout(buffer):
        yield buffer


@contextlib.contextmanager
def capture_console_output():
    """
    Context manager that captures stdout to a StringIO buffer (non-streaming).

    Usage:
        with capture_console_output() as buffer:
            print("This will be captured")
        captured_text = buffer.getvalue()

    Yields:
        io.StringIO: Buffer containing captured output
    """
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        yield buffer


def display_console_output(output: str, language: str = "log"):
    """
    Display console output in a code block.

    Args:
        output: The console output text to display
        language: Syntax highlighting language (default: "log")
    """
    st.code(output, language=language)


def render_file_content(
    file_path: Path,
    show_raw_view: bool = False,
    expanded: bool = True,
    use_text_area: bool = False
):
    """
    Render file content based on file type with appropriate formatting.

    Supports:
    - Markdown files (.md): Rendered as formatted markdown
    - JSON files (.json): Interactive JSON viewer
    - Other files: Code block or text area

    Args:
        file_path: Path to the file to render
        show_raw_view: If True, shows raw content in an expander (useful for md/json)
        expanded: Whether to expand the raw view by default
        use_text_area: If True, uses text_area for non-md/json files (non-interactive mode)

    Returns:
        bool: True if rendering succeeded, False otherwise
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        suffix = file_path.suffix.lower()

        if suffix == '.md':
            # Markdown preview
            if show_raw_view:
                st.markdown("**Markdown Preview:**")
            st.markdown(content)

            if show_raw_view:
                with st.expander("📝 Raw Markdown", expanded=False):
                    st.code(content, language="markdown")

        elif suffix == '.json':
            # JSON preview
            if show_raw_view:
                st.markdown("**JSON Preview:**")

            try:
                json_data = json.loads(content)
                st.json(json_data)

                if show_raw_view:
                    with st.expander("📝 Raw JSON", expanded=False):
                        st.code(content, language="json")
            except json.JSONDecodeError:
                # If JSON parsing fails, show as code
                st.code(content, language="json")

        else:
            # Other file types
            if show_raw_view:
                st.markdown("**Text Preview:**")

            if use_text_area:
                st.text_area("Content", content, height=400)
            else:
                st.code(content)

        return True

    except Exception as e:
        st.error(f"Could not display file: {e}")
        return False


def open_output_folder(output_dir: Path, button_key: Optional[str] = None):
    """
    Display a button to open the output folder in the system file explorer.

    Args:
        output_dir: Path to the output directory
        button_key: Optional unique key for the button (required if multiple buttons exist)

    Returns:
        bool: True if button was clicked and folder opened, False otherwise
    """
    if st.button("📂 Open Output Folder", key=button_key):
        import subprocess
        import platform

        try:
            system = platform.system()
            if system == "Windows":
                subprocess.run(["explorer", str(output_dir.resolve())])
            elif system == "Darwin":  # macOS
                subprocess.run(["open", str(output_dir.resolve())])
            else:  # Linux
                subprocess.run(["xdg-open", str(output_dir.resolve())])
            return True
        except Exception as e:
            st.error(f"Could not open folder: {e}")
            return False

    return False


def display_file_with_download(
    file_path: Path,
    show_raw_view: bool = True,
    use_text_area: bool = False
):
    """
    Display file content with a download button.

    Args:
        file_path: Path to the file to display
        show_raw_view: Whether to show raw view for markdown/JSON
        use_text_area: Whether to use text_area for other files
    """
    try:
        content = file_path.read_text(encoding='utf-8')

        # Render the file
        render_file_content(
            file_path,
            show_raw_view=show_raw_view,
            use_text_area=use_text_area
        )

        # Download button
        st.download_button(
            label=f"⬇️ Download {file_path.name}",
            data=content,
            file_name=file_path.name,
            mime="text/plain"
        )

    except Exception as e:
        st.error(f"Failed to read file: {e}")


def display_unified_output(
    output_dir: Path,
    console_output: Optional[str] = None,
    show_all_files: bool = True,
    result: Optional[Dict] = None,
    button_key_prefix: str = "output"
):
    """
    Unified output display component for both interactive and non-interactive modes.

    This component displays:
    1. Console output (if provided)
    2. File browser with selector
    3. File preview with appropriate rendering
    4. Download button
    5. Open folder button

    Args:
        output_dir: Path to the output directory
        console_output: Optional console output text to display
        show_all_files: If True, shows all files. If False, shows only last output file
        result: Optional result dictionary containing execution metadata
        button_key_prefix: Prefix for button keys to avoid conflicts
    """
    # Display console output if provided
    if console_output:
        st.markdown("#### 📟 Console Output")
        display_console_output(console_output)
        st.divider()

    # Display output files
    st.markdown("#### 📄 Output Files")

    if not output_dir.exists():
        st.warning("Output directory not found")
        return

    # Get list of output files
    output_files = sorted(output_dir.glob("*.*"), key=lambda x: x.stat().st_mtime, reverse=True)

    if not output_files:
        st.info("No output files found")
        return

    # File selection
    if show_all_files and len(output_files) > 1:
        # Show selector for multiple files
        selected_file = st.selectbox(
            "Select file to preview",
            options=output_files,
            format_func=lambda x: f"{x.name} ({_format_file_time(x)})",
            key=f"{button_key_prefix}_file_selector"
        )
    else:
        # Show only the latest file
        selected_file = output_files[0]
        st.info(f"**Latest file:** {selected_file.name}")

    # Display selected file with download button
    if selected_file:
        st.markdown("---")
        display_file_with_download(
            selected_file,
            show_raw_view=True,
            use_text_area=(len(output_files) > 1)  # Use text area when browsing multiple files
        )

    # Open folder button
    st.markdown("---")
    open_output_folder(output_dir, button_key=f"{button_key_prefix}_open_folder")

    # Display metadata if available
    if result:
        with st.expander("ℹ️ Execution Details"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Output Directory", result.get("output_dir", "N/A"))
            with col2:
                st.metric("Last Output File", result.get("last_output_file", "N/A"))


def _format_file_time(file_path: Path) -> str:
    """Helper function to format file modification time."""
    try:
        from datetime import datetime
        mtime = file_path.stat().st_mtime
        dt = datetime.fromtimestamp(mtime)
        return dt.strftime("%H:%M:%S")
    except:
        return ""
