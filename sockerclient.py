# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     
   Description :
   Author :       ianchen
   date：          
-------------------------------------------------
   Change Activity:
                   2017/11/22:
-------------------------------------------------
"""
import socket

# 创建一个socket:TCP协议
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 25532))

aa="@1039"
l=len(aa)
for i in range((128-l)):
    aa+=" "
by=bytes(aa,'utf8')

s.send(by)
pass
