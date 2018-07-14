#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/28 10:50
# 定时 爬取每日股票行情数据;
# 股票数据内容：
# 后期对单个股票做 可视化处理

import getSoup
import pymysql
import os
from bs4 import BeautifulSoup as bs
import re
import json
import requests
import formatSQL
import connect_dataBase
import time

# db连接
connectDB = connect_dataBase.ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf["stockMarket"]["host"], get_conf["stockMarket"]["user"],
                     get_conf["stockMarket"]["password"], get_conf["stockMarket"]["database"], get_conf["stockMarket"]["port"])

# 第一步, 通过东方财富网  获取 上海/深圳 所有股票的 股票代码, 存储到list中
url = 'http://quote.eastmoney.com/stocklist.html#'
soup = getSoup.getSoup(url)
uls = soup.select('div#quotesearch li')
# 正则表达式获取所有的股票代码
re1 = re.compile(r'href="http://quote.eastmoney.com/(.+?).html"')
stockCodes = re1.findall(str(uls))
# print(stockCodes)

# 第二步, 将股票代码加入到 股票搜索 的网址中
stockValues = []
for stockCode in stockCodes:
    # url = 'https://gupiao.baidu.com/stock/'+stockCode+'.html'
    url = 'https://gupiao.baidu.com/api/rails/stockbasicbatch?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&stock_code='+stockCode+''
    # print(url)
    # soup = getSoup.getSoup(url)
    response = requests.get(url)
    response.raise_for_status()
    res = response.content
    try:
        JsonDatas = json.loads(res, encoding='utf-8')
    except:
        print('数据异常,跳过')
    datas = JsonDatas['data']
    print(datas)
    for data in datas:
        # 添加当天日期(交易日), 判断采集当天是否是交易日
        if time.strftime('%w', time.localtime()) == '0':
            date = time.strftime("%Y%m%d", time.localtime())
            date = int(date) - 2
        elif time.strftime('%w', time.localtime()) == '6':
            date = time.strftime("%Y%m%d", time.localtime())
            date = int(date) - 1
        else:
            date = time.strftime("%Y%m%d", time.localtime())
        stockCode = data['stockCode']
        stockName = data['stockName']
        close = data['close']
        high = data['high']
        low = data['low']
        amplitudeRatio = data['amplitudeRatio']
        turnoverRatio = data['turnoverRatio']
        preClose = data['preClose']
        open = data['open']
        sql = 'insert into stockmarket(date,stockCode,stockName,close,high,low,amplitudeRatio,turnoverRatio,preClose,open)values("'+str(date)+'","'+str(stockCode)+'","'+str(stockName)+'","'+str(close)+'","'+str(high)+'","'+str(low)+'","'+str(amplitudeRatio)+'","'+str(turnoverRatio)+'","'+str(preClose)+'","'+str(open)+'")'
        print(sql)
        if 'None' in sql:
            print('jump this data')
        else:
            try:
                connectDB.get_fetch(conn, cur, sql)
            except:
                print('数据重复,跳过')

print('采集数据完毕')










