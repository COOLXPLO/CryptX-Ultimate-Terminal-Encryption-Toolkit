@echo off
:: ============================================================
::  CryptX – Windows Batch Launcher
::  Author : iamunknown77
:: ============================================================
title CryptX – Advanced Encryption Toolkit by iamunknown77

where python >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python is not installed or not in PATH.
    echo     Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)

if "%~1"=="" (
    python "%~dp0cryptx.py"
) else (
    python "%~dp0cryptx.py" %*
)
