# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 20:02
# @Author  : Torre
# @Email   : klyweiwei@163.com
# Description ：connect to database, return cursor and conn

import json
import pymysql
import random
import string
import os
import logging


class ConnectDatabase:
    # def __init__(self, cur):
    #     self.cur = cur

    # def get_conf(self, file='databases_conf.json'):
    def get_conf(self, file):
        with open(file, "r", encoding="utf-8") as f:
            conf = json.load(f)
        return conf

    def connect_db(self, host, user, password, db, port):
        conn = pymysql.connect(host, user, password, db, port, charset="utf8")  # 最好加上utf-8
        cur = conn.cursor()
        return conn, cur

    # 获取数据库 的表, 并存储到list中
    def getTabs(self, cur):
        sql = 'show tables'
        cur.execute(sql)
        res = cur.fetchall()
        saveTabs = []
        for tab in res:
            tab = tab[0]
            saveTabs.append(tab)
        # print(saveTabs)
        return saveTabs

    # 获取列
    def get_cols(self, table, cur):
        sql = 'desc ' + str(table) + ''
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 执行sql, 返回结果
    def get_res(self, cur, sql):
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 数据的提交
    def get_fetch(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    # 数据库关闭
    def disconnect_db(self, conn, cur):
        cur.close()
        conn.close()


# connectDB = ConnectDatabase()
# get_conf = connectDB.get_conf('databases_conf.json')
# conn, cur = connectDB.connect_db(get_conf["worldCup"]["host"], get_conf["worldCup"]["user"],
#                      get_conf["worldCup"]["password"], get_conf["worldCup"]["database"], get_conf["worldCup"]["port"])
"""测试"""
# sql = 'select * from user'
# logging.debug('Logging start')
# cur.execute(sql)
# res = cur.fetchall()
# for row in res:
#     name = row[0]
#     print(name)
# logging.debug('Logging end')
# connectDB.disconnect_db(conn, cur)
"""测试"""

# tables = ['user', 'project']
# for table in tables:
#     res = connectDB.get_cols(table, cur)
#
#     sqlCount = 'select count(*) from ' + str(table) + ''
#     print(sqlCount)
#     resCount = connectDB.get_res(cur, sqlCount)
#     for row in resCount:
#         resCount = row[0]
#     # print(res)
#     print(resCount)
#     # resCount = 5000
#     # 条数可修改
#     while resCount < 5000:
#         loop = 50000
#         for i in range(1, loop):
#             sql = ""  # 被执行的sql
#             sqlValue = ''
#             insertValue = ''
#             for row in res:
#                 col_name = row[0]
#                 col_type = row[1]
#                 index = int(col_type.rfind('('))
#                 # print(type(col_name))
#                 # print(col_name, index)
#                 if 'int' in col_type:
#                     insertValue = (insertValue + '%s') % str(random.randint(1, 50000))
#                     # print(insertValue)
#                 elif 'varchar' in col_type:
#                     # 生成随机字符串
#                     insertValue = ''
#                     insertValue = "{0}'{1}',".format(insertValue, col_name + str(random.randint(0, 999)))
#                     # insertValue = ''.join(random.sample(string.ascii_letters + string.digits, 8))
#                     # print(insertValue)
#                 elif col_type in ["decimal", "double", "numeric", "real","float"]:
#                     insertValue = (insert_sql + "%f,") % random.uniform(g(1, 999999), 999999)
#                 # sqlValue + = sqlValue
#                 sqlValue += "{0},".format(insertValue[:-1])
#             # print(sqlValue)
#             sql += "insert into {0} values ({1});".format(table, sqlValue[:-1])
#             try:
#                 connectDB.get_fetch(conn, cur, sql)
#                 resCount += 1
#                 print(resCount)
#                 if resCount == 5000:
#                     break
#                 else:
#                     continue
#             except:
#                 print("Duplicate Primary Key")
#                 continue
#             print(sql)
#     sqlCount = 'select count(*) from ' + str(table) + ''
#     resCount = connectDB.get_res(cur, sqlCount)
#     for row in resCount:
#         resCount = row[0]
#     # print(res)
#     print(resCount)
#     print("success insert into " + str(table) + " "+str(resCount) + " sqlData")








        




