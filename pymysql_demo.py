import pymysql

try:
    con = pymysql.connect(
        host='192.168.237.131',
        port=3306,
        user='ywy',
        password='123456',
        db='09_24',
        charset='utf8'
    )

    # 测试连接
    cursor = con.cursor()
    cursor.execute('select 1')
    re = cursor.fetchone()
    print(re)
    # 关闭连接
    cursor.close()
    con.close()
except pymysql.Error as e:   #
    # print(e)
    print('Error %s: %s' % (e.args[0], e.args[1]))






class MySQLClass:

    def __init__(self):
        self.get_conn()

    def get_conn(self):
        try:
            config = {
                "host": "192.168.237.131",
                "port": 3306,
                "user": "ywy",
                "password": "123456",
                "db": "09_24",
                "charset": "utf8"
            }
            self.conn = pymysql.connect(**config)  #**解包
        except pymysql.Error as e:
            print('Error %s: %s' % (e.args[0], e.args[1]))

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error %s: %s' % (e.args[0], e.args[1]))

    def test(self):
        cursor = self.conn.cursor()
        cursor.execute('select 1')
        re = cursor.fetchone()
        cursor.close()
        self.close_conn()
        return  re

    def add(self):
        try:
           # 准备sql
           sql = "insert into user(name, age) values(%s, %s)"
           # 找到cursor
           cursor = self.conn.cursor()
           # 执行sql
           cursor.execute(sql, ('Which', 20))
           # 事务提交
           self.conn.commit()
           cursor.close()
           self.close_conn()
        except:
            print('error')
            # 回滚
            self.conn.rollback()

    def delete_operate(self):
        try:
            sql = "delete from user where %s='%s'" % ('name', "Which")
            print(sql)
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
        except pymysql.Error as e:
            print('Error %s: %s' % (e.args[0], e.args[1]))
            self.conn.rollback()
    def update_operate(self):
        try:
            sql = "update user set name=%s where id=1"
            cursor = self.conn.cursor()
            # 执行的时候 传值
            cursor.execute(sql, ('Which666'))
            # print(sql)
            self.conn.commit()
        except:
            print('error')
            self.conn.rollback()
#只要你修改数据库数据 都会有事务提交和回滚
    def search_operate(self):
        sql = "select * from user where name=%s"
        cursor = self.conn.cursor()
        cursor.execute(sql, ('Which666',))
        # 返回一条数据 元祖
        result = cursor.fetchone()
        print(result)   #返回的是一个一个元祖
        # print(result['name'])   这条执行不了，会报错。
        print(cursor.description) #这个打印的是详情。
        # result = dict(zip([k[0] for k in cursor.description], cursor.fetchone()))
        # print(result)
        all = []
        for k in cursor.description:
            all.append(k[0])
        print(all)  #打印的是['id','name','age']
        re = dict(zip(all, cursor.fetchone()))
        print(re)
        print(re['age'])
        cursor.close()
        self.conn.close()

# 只能迭代一次
which = MySQLClass()
# re = which.test()
# print(re)
#which.add()
# which.delete_operate()
# which.update_operate()
which.search_operate()


