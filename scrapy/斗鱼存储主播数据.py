#-*- coding:utf-8 -*-
#_author:John
#date:2018/10/25 0:07
#softwave: PyCharm
import requests
import json
from multiprocessing import Pool
# import pymysql
import datetime
# mongo 的登陆
#import pymogo
# client = pymongo.MongoClient('localhost')
# db = client['douyu']


# mysql 数据库连接
# conn=pymysql.connect('localhost','root','ycy1234')
# cursor=conn.cursor()
# sql_database='create database if not exists `douyu`'

# sql='''
# create table `douyutag`(\
# `id` int(11) auto_increment primary key,\
# `dt` varchar(50),\
# `title` varchar(255),\
# `person` varchar(255),\
# `hotpoint` int(11) ,\
# `label` varchar(255),\
# `room` int(11)\
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
# '''
# cursor.execute(sql_)
# cursor.execute('use`douyu`')
# cursor.execute(sql)


def get_conn():
    
    conn=pymysql.connect('localhost','root','ycy1234','douyu')
    cursor=conn.cursor()
    return conn ,cursor

def close_conn(conn ,cursor):
    cursor.close()
    conn.close()

    

def single_page_info(page):
    data=[]
    sql='insert into `douyutag`(dt,title,person,hotpoint,label,room) value(%s,%s,%s,%s,%s,%s)'
    respones = requests.get('https://www.douyu.com/gapi/rkc/directory/0_0/{}'.format(page))
    datas = json.loads(respones.text)
    items = datas['data']['rl']
    cur_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    for item in items:
        data.append((cur_time,item['rn'],item['nn'], item['ol'],item['c2name'],item['rid']))
        print(item['rn'],item['nn'], item['ol'],item['c2name'],item['rid'])
        # 不保存相同时间相同主播名的记录
#         if db['host_info'].update({'主播': data['主播'], '时间': data['时间']}, {'$set': data}, True):
#             print('Save to Mongo, {}'.format(data))
#         else:
#             print('Save to Mong fail, {}'.format(data))
    # conn,cursor=get_conn()
    # cursor.executemany(sql,data)
    # conn.commit()
    # close_conn(conn,cursor)
#     print(data)

    print('已经完成第{}页'.format(page))

if __name__ == '__main__':
    for page in range(1, 201):
        single_page_info(page)
    
#     pool = Pool()
#     #多线程抓200页
#     pool.map(single_page_info, [page for page in range(1, 201)])