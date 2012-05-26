@echo off

if '%*'=='' cd & exit /b
if '%*'=='-' (
    cd /d %OLDPWD%
    set OLDPWD=%cd%
    echo.
) else (
    cd /d %*
    echo.
    if not errorlevel 1 set OLDPWD=%cd%
)

