# coding: utf-8


import pymysql

class HtmlOutputer(object):

    def dbconnect(self):
        # 打开数据库连接
        db = pymysql.connect(host="localhost", user="root", passwd="", db="myspider", use_unicode=True, charset="utf8")
        return db

    def insertdb(self, db, content):
        # 使用cursor()方法来获取操作游标
        cursor = db.cursor()
        sql  = "INSERT into dfcf_notices(`code`, `name`, `title`, `type`, `publictime`, `url`, `content`) VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
        sql = sql %(content[0], content[1], content[2], content[3], content[4], content[5], content[6])
        flag = 1
        try:
            # print(sql)
            # 运行sql
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
        except:
            flag = 0
            db.rollback()
            print("db run error")

        db.close()
        if flag:
            return True
        return False

# 测试用例
if __name__ == '__main__':
    content = ['600393', '粤泰股份', '600393:粤泰股份重大资产重组停牌进展公告', '停牌公告', '2018-05-04',
               'http://data.eastmoney.com/notices/detail/600393/AN201805031136090961,JWU3JWIyJWE0JWU2JWIzJWIwJWU4JTgyJWExJWU0JWJiJWJk.html',
               '证券代码：600393 ']
    db = HtmlOutputer().dbconnect()
    res = HtmlOutputer().insertdb(db, content)
    print(res)