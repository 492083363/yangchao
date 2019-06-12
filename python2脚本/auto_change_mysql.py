#!/usr/bin/env python
# -*- coding: utf-8 -*-
#自动切换主从数据库 
#
import MySQLdb
import time
import sys
class m_s:
    def __init__(self,host,user,password,port):
        self.host=host
        self.user=user
        self.passowrd=password
        self.port=port
    def getConn(self,db="mysql"):
        try:
            conn=MySQLdb.connect(host=self.host, user=self.user, passwd=self.passowrd, db=db, port=self.port, charset="utf8")
            cur = conn.cursor()
            return cur
        except Exception as e:
            return e
    def execSQLlock(self,*args):
        flush_sql="FLUSH TABLES WITH READ LOCK"
        cur.execute(flush_sql)
    def execIo(self,cur,command):
        cur.execute(command)
        db_pos = cur.fetchall()
        for value in db_pos:
            value=value
        return value
    def exeStop(self,cur,command):
        cur.execute(command)
        db_pos = cur.fetchall()
        return db_pos
    def execSQLstatus(self,*args):
        n=0
        self.execSQLlock(cur)
        flush_m = "flush logs"
        cur.execute(flush_m)
        while True:
            data=[]
            slave_pos=[]
            n=n+1
            exe_sql = "select Command,State,Info,Id from information_schema.processlist"
            cur.execute(exe_sql)
            plist = cur.fetchall()
            for li in range(len(plist)):
                if plist[li][0] == "Query" and plist[li][1] == "Waiting for global read lock":
                    lock_id = "kill " + str(plist[li][3])
                    print plist[li][2]
                    cur.execute(lock_id)
            slave_pos.append(self.execIo(cur1, "show master status")[1])
            data.append(self.execIo(cur1,"show slave status")[6]) ##从库的游标
            time.sleep(1)
            slave_pos.append(self.execIo(cur1, "show master status")[1])
            data.append(self.execIo(cur,"show master status")[1])##从库的游标
            print ".......",data,slave_pos
            if data[0]==data[1] and slave_pos[0]==slave_pos[1]:
                try:
                    print "第%s次判断数据已经同步....."%n
                    if n==c_time:
                        print "开始主从切换工作........"
                        self.exeStop(cur1,"stop slave") ##停止从库同步
                        new_pos=self.exeStop(cur1,"show master status")#获取新主库的FILE和POS的值,游标为还没切换前的从库
                        #print "获取新主库的FILE和POS的值,游标为还没切换前的从库",new_pos
                        self.exeStop(cur,"reset master;")##主库释放从库主从信息......
                        ##在从库执行new_change 指向新的主库
                        self.exeStop(cur1,"reset slave all")
                        new_change="change master to master_host='"+str(args[1])+"'"+",master_user='"+args[2]+"'"+",master_password='"+args[3]+"',master_port="+str(args[4])+",MASTER_LOG_FILE='"+str(new_pos[0][0])+"'"+",MASTER_LOG_POS="+str(new_pos[0][1])
                        print new_change
                        self.exeStop(cur,new_change)##在原来主库上执行change master to.....
                        #print "在原来主库上执行change master to...."
                        self.exeStop(cur,"start slave")  ##在原来主库上执行change master to.....
                        time.sleep(5)
                        s_pos=self.exeStop(cur,"show slave status;")
                        #print s_pos[0][10],s_pos[0][11]
                        if s_pos[0][10]=="Yes" and s_pos[0][11]=="Yes":
                            self.exeStop(cur1,"reset slave all")
                            print  "主从切换成功!"
                            print "\n"
                            while True:
                                print "等待其他操作完成,即将unlock tables主库......"
                                try:
                                    stop = raw_input("输入终止命令q即完成此次操作:\n")
                                    if stop == "q":
                                        sys.exit()
                                        # break
                                except Exception as e:
                                    print "good bye"

                        else:
                            print   s_pos[0][19]
                        break
                except Exception as e:
                    return e
            else:
                print "主从数据未达到一致性..........",n
                n=0
                data=[]

if __name__ =="__main__":
    c_time=int(raw_input("多少秒后进行主从切换..&gt;&gt;"))
    print "****************************************************\n"

    print "请根据提示输入指定信息:"
    m_host = raw_input("目前主库的地址:")
    m_user = raw_input("目前主库的登陆用户名:")
    m_password = raw_input("目前主库的密码:")
    m_port = int(raw_input("目前主库的端口:"))
    print "****************************************************\n"
    s_host = raw_input("目前从库的地址:")
    s_user = raw_input("目前从库的登陆用户名:")
    s_password = raw_input("目前从库的密码:")
    s_port = int(raw_input("目前从库的端口:"))
    M = m_s(m_host, m_user, m_password, m_port)
    S = m_s(s_host,s_user,s_password,s_port)
    cur = M.getConn()  ##获取主库游标
    cur1 = S.getConn()  ##获取从库游标
    print "*****************************************************\n"
    print "主从同步用户信息.........\n"
    s_user1 = raw_input("输入主从同步的用户&gt;&gt;:")
    s_password1 = raw_input("输入主从同步的密码:")
    s_port1 = int(raw_input("输入主从同步的端口:"))

    M.execSQLstatus(cur,s_host,s_user1,s_password1,s_port1)
