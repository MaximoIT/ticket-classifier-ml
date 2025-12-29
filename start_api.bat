@echo off
cd /d "%~dp0"
python -m uvicorn src.api.app:app
pause
