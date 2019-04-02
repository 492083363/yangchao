#coding=utf-8
#安装pywin32-224包
#Microsoft Windows的Python扩展提供对大部分Win32 API的访问，创建和使用COM对象的能力以及Pythonwin环境。

import win32com
import win32com.client
def makeexcel(name):
    print(name)
    excel=win32com.client.Dispatch("Excel.Application")
    wk=excel.Workbooks.Add()    #加一张表格
    nowwk=wk.ActiveSheet #当前的焦点表格
    excel.Visible=True          #显示
    for i in range(1,10):
        nowwk.Cells(1,i).value=name+str(i) #插入数据
    filename="E:/pacong/python_51cto/autooffice/"+name+".xls"
    wk.SaveAs(filename)
    wk.Close(True)  # 关闭
    excel.Application.Quit()  # 退出

#dic={"a":1,"b":2,"c":3,"d":4}
names=["a","b","c","d"]
for name in names:
    makeexcel(name)

