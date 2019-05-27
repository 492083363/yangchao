#检测机器IP地址 
@echo off
for /f "tokens=4" %%a in ('route print^|findstr 0.0.0.0.*0.0.0.0') do (
 set IP=%%a
)
echo 你的局域网IP是：
echo %IP%
pause>nul
