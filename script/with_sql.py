#!/usr/bin/env python3
import pymysql

#打开数据库连接
db_saas={
		"host":"localhost",
		"user":"root",
		"password":"123123",
		"db":"hatgrid",
		"charset":"utf8",
        "ssl":{'ssl':{}}  
	}

connection = pymysql.connect(**db_saas)
with connection:
    with connection.cursor() as cursor:
        sql="select * from hatgrid_grid"
        cursor.execute(sql)
        connection.commit()
        for row in cursor:
            print (row)