import pymysql

class sqlConnect:

    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='interface', charset='utf8')
        self.cur = self.db.cursor()

    # 查询一条数据
    def search_one(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        print(result)
        self.cur.close()

    # 查询所有数据
    def search_all(self, sql):
        rows = self.cur.execute(sql)
        print(rows)


    def decode(self):
        pass

if __name__ == '__main__':
    mysql = sqlConnect()
    mysql.search_one("select * from sys_user where username = 'wangzhaowu' and 1=2")