#vb脚本，配合zabbix-agent，监控windows上mysql数据库状态

Set objFS = CreateObject("Scripting.FileSystemObject")
Set objArgs = WScript.Arguments
str1 = getCommandOutput("C:\Program Files\MySQL\MySQL Server 5.1\bin\mysqladmin.exe -uroot -pxxxx  extended-status")     #这里注意写明mysqladmin程序的绝对路径和root用户密码
Arg = objArgs(0)
str2 = Split(str1,"|")
 
For i = LBound(str2) to UBound(str2)
 
If Trim(str2(i)) = Arg Then   
WScript.Echo TRIM(str2(i+1))
Exit For
End If
next
 
 
Function getCommandOutput(theCommand)
 
Dim objShell, objCmdExec
Set objShell =CreateObject("WScript.Shell")
Set objCmdExec = objshell.exec(thecommand)
getCommandOutput =objCmdExec.StdOut.ReadAll
 
end Function
