@echo off
IF EXIST "%PROGRAMFILES(X86)%" (SET BIT=x64) ELSE (SET BIT=x86)
bin\win_ansi_cmd\%BIT%\ansicon.exe python main\__init__.py
