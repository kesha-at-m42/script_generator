@echo off
REM Launch Module Editor (Windows)
echo.
echo ========================================
echo   Module Editor Launcher
echo ========================================
echo.
echo Starting module editor...
echo.

cd /d "%~dp0"
call venv\Scripts\activate.bat
streamlit run dashboard\run_module_editor.py

pause
