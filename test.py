# -*- coding: utf-8 -*-
# @Time    : 2018/7/14 14:31
# @Author  : Torre
# @Email   : klyweiwei@163.com
import time
import datetime

date = time.strftime('%w', time.localtime())
print(date)
if date == '0':
    print('周末')
    date = time.strftime("%Y%m%d", time.localtime())
    print(int(date)-2)
elif date == '6':
    date = time.strftime("%Y%m%d", time.localtime())
    print(int(date)-1)
else:
    date = time.strftime("%Y%m%d", time.localtime())
# print(date)