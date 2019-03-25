#coding=utf-8
#安装pywin32-224包
#Microsoft Windows的Python扩展提供对大部分Win32 API的访问，创建和使用COM对象的能力以及Pythonwin环境。

import win32com
import win32com.client
def makeword(name):
    print(name)
    word=win32com.client.Dispatch("Word.Application")
    doc=word.Documents.Add()        #插入文档
    word.Visible=True               #可见

    rng=doc.Range(0,0)          #开始位置
    rng.InsertAfter(u"尊敬的%s先生\n"%name)#匹配字符串，u代表unicode,匹配名字
    rng.InsertAfter(u"          哈哈哈哈哈哈")  # 插入字符串

    filename="E:/pacong/python_51cto/autooffice/"+name+".doc"   #保存名称
    doc.SaveAs(filename)    #保存
    doc.Close(True) #关闭
    word.Application.Quit()  # 退出

names=["a","b","c","d"]
for name in names:
    makeword(name)

