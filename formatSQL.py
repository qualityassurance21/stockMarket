#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Torre Yang Edit with Python3.6
# @Email  : klyweiwei@163.com
# @Time   : 2018/6/19 10:22
# 适用于所有 json相关爬虫的数据采集 任务
import connect_dataBase

# db连接
connectDB = connect_dataBase.ConnectDatabase()
get_conf = connectDB.get_conf('databases_conf.json')
conn, cur = connectDB.connect_db(get_conf["stockMarket"]["host"], get_conf["stockMarket"]["user"],
                     get_conf["stockMarket"]["password"], get_conf["stockMarket"]["database"], get_conf["stockMarket"]["port"])


# def getTabs():
#     sql = 'show tables'
#     res = connectDB.get_res(cur, sql)
#     saveTabs = []
#     for tab in res:
#         tab = tab[0]
#         saveTabs.append(tab)
#     # print(saveTabs)
#     return saveTabs
# print(connectDB.getTabs(cur))

# 一键 获取表, 并为数据的存储做铺垫
# tabs = connectDB.getTabs(cur)
# for tab in tabs:
#     sqll = 'insert into '+ tab
#     print(sqll)

# 数据的格式化 很重要 , ajax请求json爬取数据自动生产插入SQL语句 "'+str(dt)+'"
def formatSQL(table, cur):
    # table名字
    resCon = connectDB.get_cols(table, cur)
    saveConls = []
    saveVals = []
    for row in resCon:
        col = row[0]
        # print(col)
        # 保存值列表
        val = '"\'+str(' + str(col) + ')+\'"'
        saveVals.append(val)
        saveValss = ','.join(saveVals)
        # 保存字段列表
        saveConls.append(col)
        saveConlss = ','.join(saveConls)
    # return saveConls, saveVals

        # col = '"\'+str('+ str(col) +')+\'"'
        # saveConls.append(col)
        # saveConlss = ','.join(saveConls)
    sql = 'insert into '+table+''+'('+saveConlss+')'+ 'values('+saveValss+')'
    return sql


# # 函数 的调用
if __name__ == '__main__':
    sql = formatSQL('stockmarket', cur)
    print(sql)




