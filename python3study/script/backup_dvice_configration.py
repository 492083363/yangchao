#! env python
# coding=utf-8
#
#ver2.0 
#使用ftp方式备份华为交换机配置文件
#python3版本
from ftplib import FTP
import time
import os
import sys


dic = {
    'tongjiju': ['10.42.243.1',
                 '10.42.243.2',
                 '10.42.243.3',
                 '10.42.243.4',
                 '10.42.243.5',
                 '10.42.243.6',
                 '10.42.243.7',
                 '10.42.243.8',
                 '10.42.243.9',
                 '10.42.243.10',
                 '10.42.243.11',
                 '10.42.243.12',
                 '10.42.243.13',
                 '10.42.243.14',
                 '10.42.243.22',
                 '10.42.243.23',
                 '10.42.243.24',
                 '10.42.243.27',
                 '10.42.243.31',
                 '10.42.243.32',
                 '10.42.243.34',
                 '10.42.243.50'],
    'caizheng': ['192.168.10.11',
                 '192.168.10.17',
                 '192.168.10.16',
                 '192.168.10.18',
                 '192.168.10.19',
                 '192.168.10.20',
                 '192.168.10.22',
                 '192.168.10.23',
                 '192.168.10.24',
                 '192.168.10.26',
                 '192.168.10.27',
                 '192.168.10.28',
                 '192.168.10.30',
                 '192.168.10.31',
                 '192.168.10.32',
                 '192.168.10.33',
                 '192.168.10.34',
                 '192.168.10.35',
                 '192.168.10.36',
                 '192.168.10.37'],
    'jianhangjiankong': ['172.31.212.3',
                         '172.31.212.4',
                         '172.31.222.2',
                         '172.31.223.2',
                         '172.31.224.2',
                         '172.31.225.2',
                         '172.31.226.2',
                         '172.31.212.5',
                         '172.31.212.30'],
    'jingzhouQinQ': ['192.168.200.10',
                     '192.168.200.11',
                     '192.168.200.12',
                     '192.168.200.13',
                     '192.168.200.14',
                     '192.168.200.15',
                     '192.168.200.16'],

    # jingzhoushilian': ['172.31.221.67',
    #                   '172.31.221.68',
    #                    '172.31.221.69',
    #                    '172.31.221.70',
    #                    '172.31.221.71',
    #                    '172.31.221.72'],

    'jiancewang': ['172.31.218.2'],
    'guoganjiance': ['172.31.220.2', '172.31.220.3'],
    'tongjiyiyuan': ['172.31.219.2'],
    'tushuguan': ['172.31.211.2'],
    'zhuanwang': ['172.31.214.2'],
    'dishui': ['172.31.216.12',
               '172.31.216.2',
               '172.31.216.11',
               '172.31.216.12',
               '172.31.216.13',
               '172.31.216.14',
               '172.31.216.38',
               '172.31.216.23',
               '172.31.216.24',
               '172.31.216.40',
               '172.31.216.39',
               '172.31.216.37',
               '172.31.216.34',
               '172.31.216.33',
               '172.31.216.19',
               '172.31.216.20',
               '172.31.216.35',
               '172.31.216.36',
               '172.31.216.9'],
    'jifang': ['192.168.1.7',
               '192.168.1.8',
               '192.168.1.11',
               '192.168.1.13',
               '172.31.205.29',
               '192.168.1.5',
               '192.168.1.6',
               '192.168.1.12']
}


def save(hosts, ftp):
    url = 'G:\设备资料备份\{}'.format(hosts)
    Today = time.strftime("%Y-%m-%d", time.localtime())
    clock = time.strftime("%H:%M:%S", time.localtime())
    ftp_error_log = 'G:\设备资料备份\备份日志\{}.txt'.format(Today)
    if not os.path.exists(url):
        os.mkdir(url)
    for host in dic[hosts]:
        os.chdir(url)
        if not os.path.exists(host):
            os.mkdir(host)
            os.chdir(host)
        else:
            os.chdir(host)
        try:
            ftp.connect(host=host, port=21)
            ftp.login(user='admin', passwd='ecz@1234')
            bufsize = 1024
            filename = "{}.zip".format(Today)
            file_handle = open(filename, "wb").write
            ftp.retrbinary("RETR vrpcfg.zip", file_handle, bufsize)
            print("login " + host)
            print(ftp.getwelcome())
            print(host + " ftp down ok")
        except Exception as e:
            print('{} is loss , msg:-{},time is {}'.format(host, e, clock))
            print('{} is loss , msg:-{},time is {}'.format(host, e, clock),file=open(ftp_error_log,'a'))
            


def main():
    ftp = FTP()
    # ftp.set_debuglevel(2)
    # 0主动模式 1 #被动模式
    ftp.set_pasv(0)
    for hosts in dic.keys():
        save(hosts, ftp)
    # 关闭调试模式
    # ftp.set_debuglevel(0)
    ftp.quit()
    ftp.close()
    #ftp_error_log.close()

if __name__ == '__main__':
    main()
