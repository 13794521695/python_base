import  pymysql
# con = pymysql.connect(
#     host = '192.168.237.131',
#     port = 3306,
#     user = 'ywy',
#     password ='123456',
#     db = '09_24',
#     charset = 'utf8'
# )
#
# cursor = con.cursor()
# cursor.execute('select 1')
# re =  cursor.fetchone()
# print(re)

class MysqlClass:
    def __init__(self):
        self.get_conn()
    def get_conn(self):
        try:
            config = {
                "host":"192.168.237.131",
                "port":3306,
                "user":"ywy",
                "password":"123456",
                "db":"09_24",
                "charset":"utf8"
            }
            self.conn = pymysql.connect(**config)
        except pymysql.Error as e:
            print('Error %s:%s'%(e.args[0],e.args[1]))
    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('Error  %s:%s'%(e.args[0],e.args[1]))

    def test(self):
        cursor = self.conn.cursor()
        cursor.execute('select 1')
        re = cursor.fetchone()
        print(re)

    def add(self):
        try:
            cursor = self.conn.cursor()
            sql = "insert into  user(name,age) values(%s,%s)"
            cursor.execute(sql,('ywy',25))
            self.conn.commit()
            cursor.close()
            self.close_conn()
            print('add success!')
        except pymysql.Error as  e:
            print('Error: %s:%s'(e.args[0],e.args[1]))
            self.conn.rollback()
    def delete(self):
        try:
            cursor = self.conn.cursor()
            sql = "delete from  user  where name = %s"
            cursor.execute(sql,("liming"))
            self.conn.commit()
            cursor.close()
            self.close_conn()
            print("delete success")
        except pymysql.Error as  e:
            print("Error: %s:%s"(e.args[0],e.args[1]))
            self.conn.rollback()
    def change(self):
        try:
            cursor = self.conn.cursor()
            sql = "update  user set name = %s where id = 5"
            cursor.execute(sql,("liming"))
            self.conn.commit()
            cursor.close()
            self.close_conn()
            print("update success")
        except pymysql.Error as e:
            print("Error: %s:%s"(e.args[0],e.args[1]))
            self.conn.rollback()
    def search(self):
        sql = "select * from user where name = %s"
        cursor = self.conn.cursor()
        cursor.execute(sql,("lim"))
        result = cursor.fetchone()
        print(result)  #打印的是(6,'lim',28)  元祖
        #print(result[name])   这条打印不了，会报错
        print(cursor.description)  #这个打印的是详情
        all  = []
        for k  in cursor.description:
            all.append(k[0])           #打印 id name age
        print(all)            #打印的是['id','name','age']
        print(result)
        re = dict(zip(all,result))
        print(re)


































if __name__ == '__main__':
    which = MysqlClass()
    which.test()  #成功
    #which.add()   #成功
    #which.delete()  #成功
    #which.change()  #成功
    which.search()
