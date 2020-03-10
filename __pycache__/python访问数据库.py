#mysqlclient库，安装：pip install mysqlclient==1.3.12
#获取数据记录  fetchone，，fetchmany，，fetchall
#确保数据库启动 service mysqld status

import MySQLdb
#创立链接
conn = MySQLdb.connect(
    host='192.168.1.104',
    user='a',
    passwd='b',
    db = 'plesson',
    charset='utf8' #编码格式
)

c = conn.cursor()  #创建油标对象
#读取数据
c.execute('select * from sq_course')

# row = c.fetchone()  #返回第一条查询结果
# print(row)

# row = c.fetchone()  #返回第一条查询结果
# print(row)

#for i in range(100)  执行100次
#全部展示出来
for i in range(c.rowcount):
    row = c.fetchone()  
    print(row)


rows= c.fetchall()  #返回元组，没有分行，如果数据量大，可能就奔溃了
print(rows)

for i in range(c.rowcount):
    rows = c.fetchmany(100)  #一次一百行
    print(rows)

#判断有没有添加数据
for i in range(c.rowcount):
    row = c.fetchone()  
    if row[1]== 'pythone':
        print("1111")
        break


#插入数据
c.execute("insert into sq_course(name,'desc',display_idx) values('haha','s',6)")

conn.commit()  #数据有变化的都要加

#插1000条,f就是格式化，用到变量的写法，x+1是因为不想从0开始
for x in range(1000):
    c.execute(f"insert into sq_course(name,'desc',display_idx) values('测试课程{x+1}','s',6)")

conn.close() #不加也会自动关闭

