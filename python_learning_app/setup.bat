@echo off
REM Setup script for Python Learning App (Windows)

echo ======================================
echo Python Learning App - Setup
echo ======================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed.
    echo Please install Python 3.6 or higher from https://www.python.org/
    pause
    exit /b 1
)

REM Display Python version
python --version

echo.
echo ======================================
echo Setup Complete!
echo ======================================
echo.
echo To start learning Python, run:
echo   python main.py
echo.
echo Happy learning!
echo.
pause
