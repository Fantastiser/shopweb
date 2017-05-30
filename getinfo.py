# -*- coding: utf-8 -*-
import tools
import sys
import random
reload(sys)
sys.setdefaultencoding('utf8')
def filter():
    # SELECT
    # pName, writer, iprice, plmg, item.id, pubTime
    # from item, kinds
    # where
    # kinds.kind = "小说" and item.cld = kinds.id and 20 <= iprice <= 50
    name = "小说"
    # 书的类型
    vary = ''
    sort = '2'
    minprice = '20'
    maxprice = '50'
    result = {}
    list0_1 = ['itemid', 'name', 'author', 'iPrice', 'plmg','pubTime']
    list1 = []
    if vary == "":
        list0 = ['id', 'pName', 'writer', 'iPrice', 'plmg','pubTime']
        list = ['pName', 'cld', 'pSn', 'PDesc']
        for i in list:
            if i == 'cld':
                sql = "SELECT item.id, pName, writer, iPrice, plmg, pubTime from item, kinds where kinds.kind = '" + str(
                    name) + " 'and item.cld = kinds.id and " + str(minprice) + "<iPrice<" + str(maxprice)
                get = tools.searchDB(sql=sql)
                for ges in get:
                    dict={}
                    for it in range(0, len(list0)):
                        dict[list0_1[it]] = str(ges[it])
                    list1.append(dict)
            elif i =='pName':
                data = tools.searchDB('item', columns=list0, where=str(i) + " like'%" + str(name) + "%'" +"and "+str(minprice)+"<iPrice<"+str(maxprice))
                if data != ():
                    for ges in data:
                        dict={}
                        for it in range(0, len(list0)):
                            dict[list0_1[it]] = str(ges[it])
                        if dict not in list1:
                            list1.append(dict)
            else:
                data = tools.searchDB('item', columns=list0, where=str(i) + " ='" + str(name) + "'and " + str(minprice) + "<iPrice<" + str(maxprice))
                if data != ():
                    for ges in data:
                        dict = {}
                        for it in range(0, len(list0)):
                            dict[list0_1[it]] = str(ges[it])
                        if dict not in list1:
                            list1.append(dict)

    else:
        k = ['pName','PDec']
        for i in k:
            sql=  "SELECT pName, writer, iPrice, plmg, item.id, pubTime from item, kinds where kinds.kind = '"+str(vary)+" 'and item.cld = kinds.id and "+str(minprice)+"<iPrice<"+str(maxprice)+"and"+str(i) + " like'%" + str(name) + "%'"
            data = tools.searchDB(sql=sql)
            if data!=():
                for ges in data:
                    dict = {}
                    for it in range(0, len(list0_1)):
                        dict[list0_1[it]] = str(ges[it])
                    if dict not in list1:
                        list1.append(dict)
    if sort =='0':
        result ['data'] =list1
    elif sort == '3':
        result['data'] = sorted(list1, key=lambda list1: list1['iPrice'])
    elif sort =='4':
        result['data'] = sorted(list1, key=lambda list1: list1['iPrice'], reverse=True)
    elif sort == '1':
        result['data'] = sorted(list1, key=lambda list1: list1['pubTime'])
    elif sort == '2':
        result['data'] = sorted(list1, key=lambda list1: list1['pubTime'],reverse=True)

filter()
 # result['data'] = list1
# x= [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
# sorted_x = sorted(x, key=operator.itemgetter('name'))
# print sorted_x
# #[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
# sorted_x = sorted(x, key=operator.itemgetter('name'), reverse=True)
# print sorted_x
#[{'age': 39, 'name': 'Homer'}, {'age': 10, 'name': 'Bart'}]
# sorted_x = sorted(x, key=lambda x : x['age'])
# print sorted_x
# #[{'age': 10, 'name': 'Bart'}, {'age': 39, 'name': 'Homer'}]
# sorted_x = sorted(x, key=lambda x : x['age'], reverse=True)
# print sorted_x
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


# for i in range(1, 11):
#     kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
#     item = tools.searchDB('item', ['pName', 'min(isHot)'], where="cld = '" + str(i) + "'")
#     print item
def item(id=''):
    result = {'data':{},'msg':''}
    sqlresult = tools.searchDB('item',
                               ['pName', 'pSn', 'cld', 'mPrice', 'iPrice', 'writer', 'publisher', 'pubTime', 'plmg',
                                'descpic', 'pDesc'], where="id='" + str(id) + "'")
    if sqlresult != ():
        result['msg'] = 'sucess'
        result['data']['itemname'] = sqlresult[0][0]
        result['data']['itemid'] = sqlresult[0][1]
        result['data']['itemcategory'] = tools.searchDB('kinds', ['kind'], where="id=" + str(sqlresult[0][2] ))[0][0]
        result['data']['mprice'] = sqlresult[0][3]
        result['data']['iprice'] = sqlresult[0][4]
        result['data']['author'] = sqlresult[0][5]
        result['data']['publisher'] = sqlresult[0][6]
        result['data']['pubTime'] = sqlresult[0][7]
        result['data']['itempic'] = sqlresult[0][8]
        result['data']['descpic'] = sqlresult[0][9]
        result['data']['description'] = sqlresult[0][10]
    else:
        result['msg'] = 'fail'

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