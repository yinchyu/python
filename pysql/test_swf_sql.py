import pymysql
# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect(host="localhost", user="root", password="ycy1234", database="radio")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()
print("Database version : %s " % data)
# 实现数据库的查找操作
# sql_list = ["SELECT * FROM course","UPDATE user SET name = 'Bob' WHERE id = 1",
# "DELETE FROM user WHERE id  = 1","INSERT INTO user(name)VALUES ('Mac')"]
# #创建数据表
# sql_list = ["""
# CREATE TABLE USER1 (
# id INT auto_increment PRIMARY KEY ,
# name CHAR(10) NOT NULL UNIQUE,
# age TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;
# """]
#
#
# for sql in sql_list:
#     try:
#         # 执行SQL语句
#         cursor.execute(sql)
#         # 获取所有记录列表
#         results = cursor.fetchall()
#         for row in results:
#             print(row)
#     except:
#         print("Error: unable to fecth data")

# sql = "INSERT INTO USER1(name, age) VALUES (%s, %s);"
# data = [("Alex", 18), ("Egon", 20), ("Yuan", 21)]
# try:
#    cursor.executemany(sql,data)
#    db.commit()
# except Exception as e:
#     db.rollback()

## 读取数据
def check_english(string):
    for apha in string:
        if 0<ord(apha)<128:
            continue
        else:
            return False
    else:
        return  True


getdat="select Id , text1 from voice_tmp limit 10000;"
cursor.execute(getdat)
datalist=cursor.fetchall()
with open("eng.txt","w+",encoding="utf8")as fw_eng:
    with open("chn.txt","w+",encoding="utf8")as fw_chn:
        for i in datalist:
            if i[1]=="" or i[1] is None:
                continue
            id= i[0]
            text=i[1].decode("utf-8")
            if check_english(text):
               fw_eng.write(id+"\t"+text+"\n")
            else:
               fw_chn.write(id + "\t" + text + "\n")





cursor.close()
# 关闭数据库连接
db.close()
