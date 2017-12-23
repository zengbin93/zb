# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------------
Database Connector
1. use sqlalchemy.create_engine to create database engine
2. connect to database
3. execute SQL
4. close connection
----------------------------------------------------------------------------------
"""

import os
import subprocess
import pandas as pd
from sqlalchemy import create_engine


"""
----------------------------------------------------------------------------------
Mongodb Connector
----------------------------------------------------------------------------------
"""
class MongoConnector:
    """MongoDB"""
    from pymongo import MongoClient
    client = MongoClient('localhost', 27107)
    # client = MongoClient('mongodb://localhost:27017/')
    db = client['tes_database']
    collection = db['test_collection']

"""
----------------------------------------------------------------------------------
SQLite3 Connector
----------------------------------------------------------------------------------
"""
import sqlite3


class SQLiteConnector:
    """SQLite数据库连接器"""
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def execute_sql_with_commit(self, sql):
        """执行sql，并commit"""
        self.cursor.execute(sql)
        self.conn.commit()

    def select_to_df(self, sql):
        """执行sql查询语句，返回DataFrame"""
        datas = pd.read_sql(sql, con=self.conn)
        return datas

    def df_to_db(self, df, table_name, if_exists='fail'):
        """将DataFrame数据保存到数据库"""
        df.to_sql(table_name, con=self.conn, index=False, if_exists=if_exists)

    def vacuum(self):
        """删除数据后释放空间"""
        self.cursor.execute('VACUUM')
        self.conn.commit()

    def close(self):
        self.conn.close()


"""
----------------------------------------------------------------------------------
Oracle Connector
cx_Oracle is needed, if do not have one, execute 'pip install cx_Oracle'.
----------------------------------------------------------------------------------
"""
try:
    import cx_Oracle
except ImportError:
    os.system('pip install cx_Oracle')
    import cx_Oracle

class OracleConnector:

    def __init__(self, user, pw, ip, service):
        # 连接oracle数据库
        self.conn = cx_Oracle.connect(user, pw, ip + '/' + service)
        # conn = cx_Oracle.connect('c##bzeng/c##bzeng@192.168.31.103/orcl103')
        # 获取cursor
        self.cursor = self.conn.cursor()
        # 使用sqlalchemy创建数据库引擎
        self.ora = create_engine("oracle://%s:%s@%s:1521/%s" % (user, pw, ip, service))


    def read_sql(self, sql):
        """读取查询语句的结果"""
        df = pd.read_sql(sql, con=self.ora)
        return df


    def to_sql(self, df, table=None):
        assert table is not None, "table变量不能为空，请填入表名"
        df.to_sql(name=table, con=self.ora, if_exists='append')


    def close(self):
        self.conn.close()



"""
----------------------------------------------------------------------------------
Mysql Connector
----------------------------------------------------------------------------------
"""


class MysqlConnector:
    def __init__(self):
        try:
            import pymysql
        except ImportError:
            subprocess.run(['pip', 'install', 'pymysql'])
            import pymysql

    # # 创建连接
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='tkq1', charset='utf8')
    # # 创建游标
    # cursor = conn.cursor()
    # # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("select * from tb7")

def mysql_test():
    import pymysql

    host = 'localhost'
    username = 'root'
    password = '1111'
    db_name = 'test1'

    connection = pymysql.connect(host=host,
                                 user=username,
                                 password=password,
                                 charset='utf8',
                                 db=db_name)
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('select * from table')
        results = cursor.fetchall()
        for row in results:
            print(row[0], row[1], row[2], row[3], sep='\t')
        conn.commit()
        conn.close()

