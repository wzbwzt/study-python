#!/usr/bin/python3
 
import pymysql
 
# 打开数据库连接
db = pymysql.connect(host='localhost',
                             user='root',
                             password='123123',
                             database='core_test',
                             cursorclass=pymysql.cursors.DictCursor)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# SQL 插入语句
sql = """
INSERT INTO `core_test`.`sys_menu`( `menu_name`, `url`, `menu_id`, `menu_type`) 
VALUES ('人员角色_test', NULL, 0x53595354454D2D41555448, 0);
"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
   print("success")
except BaseException as error:
   # 如果发生错误则回滚
   db.rollback()
   print("failed",error)
 
# 关闭数据库连接
db.close()

# # 使用 execute()  方法执行 SQL 查询 
# cursor.execute("SELECT * from sys_user where id=73 ")
 
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
 
# print ("Database version : %s " % data)
 
# # 关闭数据库连接
# db.close()