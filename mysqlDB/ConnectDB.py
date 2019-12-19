import pymysql

# 创建链接
conn = pymysql.connect("192.168.100.252", "paohe", "paohe!@#", "seed")
# 使用 cursor() 方法创建游标，用于执行sql语句并获得结果
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : ", data)

try:
    cursor.execute("select * from ad_news")
    result = cursor.fetchall()
    for row in result:
        print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17])
except:
    print("Error: unable to fecth data")

# 关闭连接
conn.close()
