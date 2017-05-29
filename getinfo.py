# -*- coding: utf-8 -*-
import tools
import sys
import random
reload(sys)
sys.setdefaultencoding('utf8')
def filter(name):
    result = {}
    dict={}
    list1=[]
    list0=['id','pName','pSn','cld','pNum','mPrice','iPrice','pDesc','plmg','pubTime','ishow','isHot']
    list= ['pName','cld','pSn','PDesc']
    for i in list:
        if i =='cld':
            kinds = tools.searchDB('kinds',['id','kind'])
            for kind in kinds:
                if name == str(kind[1]):
                    get = tools.searchDB(tableName='item',columns=[],where="cld ='"+str(kind[0])+"'" )
                    for ges in get:
                        for it in range(0, len(list0)):
                            dict[list0[it]]=str(ges[it])
                        if dict not in list1:
                            list1.append(dict)


        else:

            data = tools.searchDB('item',columns=[],where = str(i) +" like'%" +str(name)+"%'")
            if data!=():
                for ges in data:
                    for it in range(0, len(list0)):
                        dict[list0[it]] = str(ges[it])
                    # if dict not in list1:
                    if dict not in list1:
                        list1.append(dict)
    result['data'] = list1
    print result
def index_find():
    list = []
    list2 = []
    for i in range(1, 11):
        kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
        list.append(kind)
        item = tools.searchDB('item', ['pName','min(isHot)'], where="cld = '" + str(i) + "'")
        if item != ():
            list2.append(item[0][0])
    print list2


a = random.randint(1, 10)
if a > 5:
    b = random.randint(1, a - 1)
else:
    b = random.randint(a + 1, 10)
titlename1 = tools.searchDB('kinds', ['kind'], where="id = '" + str(a) + "'")[0][0]
print a
titlename2 = tools.searchDB('kinds', ['kind'], where="id = '" + str(b) + "'")[0][0]
item = tools.searchDB(sql='select pName,mPrice,iPrice,plmg from item where cld = {0} ORDER BY isHot DESC '.format(str(a)))
# 插入图片
# import MySQLdb as mdb
#
#
# class BlobData:
#     def __init__(self):
#         self.conn = mdb.connect(host='localhost',user='root',passwd='chenanzhe',db='web',port=3306,charset='utf8')
#
#     def __del__(self):
#         try:
#             self.conn.close()
#         except:
#             print "close database error"
#
#     def closedb(self):
#         self.conn.close()
#
#     def setup(self):
#         cursor = self.conn.cursor()
#         try:
#             cursor.execute(
#                 "Create table if not exists picture(id int(3) primary key auto_increment, pic_name varchar(20), data longblob) engine=MyISAM default charset = utf8;")
#         except Exception, e:
#             print "create database error:", e
#         finally:
#             cursor.close()
#
#     def teardown(self):
#         cursor = self.conn.cursor()
#         try:
#             cursor.execute("drop table picture")
#         except Exception, e:
#             print "drop database error", e
#         finally:
#             cursor.close()
#
#     def testRWBlobData(self):
#         name = '1.jpg'
#         fil = open(name, 'rb')
#         b = fil.read()
#         fil.close()
#
#         cursor = self.conn.cursor()
#         cursor.execute("Insert into picture(pic_name,data) values(%s,%s)", (name,mdb.Binary(b)))
#         # cursor.execute("select data from picture order by id desc limit 1")
#         # d = cursor.fetchone()[0]
#         # cursor.close()
#         #
#         # f = open("2.jpg", 'wb')
#         # f.write(d)
#         # f.close()
#
#
# if __name__ == "__main__":
#     test = BlobData()
#
#     try:
#         test.setup()
#         test.testRWBlobData()
#         # test.teardown()
#     finally:
#         test.closedb()