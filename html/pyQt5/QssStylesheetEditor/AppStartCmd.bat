@echo off
:: 统一起始目录,默认起始位置是文件所在目录,管理员权限运行时,默认位置是C:\windows\system32
cd /d %~dp0  
set cwd=%cd%
set py=libpython
set app=main
set path=.
call %py%\python.exe scripts\%app%.pyc
pause


::ws.run "cmd /c copy C:\a.txt D:\ /y",0,1
::wscript.sleep 1000