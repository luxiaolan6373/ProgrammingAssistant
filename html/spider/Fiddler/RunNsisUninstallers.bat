@ECHO OFF
SETLOCAL EnableDelayedExpansion
FOR %%G IN (%*) DO (
    SET uninstaller=%%G
    SET uninstaller_dir=%%~dpG
    SET uninstaller_dir_trimmed=!uninstaller_dir:~0,-1!
    !uninstaller! /S _?=!uninstaller_dir_trimmed!
    IF !ERRORLEVEL! NEQ 0 (
        EXIT /B 1
    ) ELSE (
        DEL /F /Q !uninstaller!
    )
)