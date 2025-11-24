"""
Development runner for Streamlit UI with auto-reload
Watches for changes in Python files and restarts the server

Usage:
    python run_ui_dev.py
"""

import subprocess
import sys
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class StreamlitReloader(FileSystemEventHandler):
    """Handles file system events and restarts Streamlit"""

    def __init__(self):
        self.process = None
        self.restart_server()

    def restart_server(self):
        """Kill and restart the Streamlit server"""
        if self.process:
            print("🔄 Restarting Streamlit server...")
            self.process.terminate()
            self.process.wait()

        print("🚀 Starting Streamlit server...")
        self.process = subprocess.Popen(
            [sys.executable, "-m", "streamlit", "run", "pipeline_ui.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print("✅ Server started")

    def on_modified(self, event):
        """Called when a file is modified"""
        if event.is_directory:
            return

        # Only restart for Python files
        if event.src_path.endswith('.py'):
            print(f"📝 Detected change: {event.src_path}")
            time.sleep(0.5)  # Debounce
            self.restart_server()


if __name__ == "__main__":
    print("="*70)
    print("🔧 Streamlit Development Server with Auto-reload")
    print("="*70)
    print("\nWatching for changes in:")
    print("  - pipeline_ui.py")
    print("  - core/*.py")
    print("  - utils/*.py")
    print("\nPress Ctrl+C to stop\n")

    # Create and start the reloader
    event_handler = StreamlitReloader()
    observer = Observer()

    # Watch current directory and subdirectories
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping server...")
        if event_handler.process:
            event_handler.process.terminate()
        observer.stop()

    observer.join()
    print("✅ Server stopped")
