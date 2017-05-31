# -*- coding: utf-8 -*-
import tornado.web
from tornado import escape
import json
import datetime
import tools
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LoginWeb(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if (username != "" and password != ""):
            name = tools.searchDB('users', ['username'], where="username = '" + username + "'")
            email = tools.searchDB('users', ['email'], where="username = '" + username + "'")
            if name!= () or email!=():
                if username == name[0][0].decode('utf-8') or username == email[0][0]:
                    password_0 = tools.searchDB('users', ['password'], where="password = '" + password + "'")
                    password0 = ''
                    if password_0!=():
                        password0 = password_0[0][0]
                    if password0 ==password:
                        result = {"state": "true", "text": "登录成功"}
                    else:
                        result = {"state": "false", "text": "用户名或密码错误"}
                else:
                    result = {"state": "false", "text": "用户名或密码错误"}
            else:
                result = {"state": "false", "text": "用户名或密码错误"}
        else:
            result = {"state": "false", "text": "请填写完整用户名和密码"}
        self.write(escape.json_decode(json.dumps(result)))

class Move(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("information")
        result = {}
        list1 = []
        list0 = ['id', 'pName', 'writer', 'pSn', 'cld', 'pNum', 'mPrice', 'iPrice', 'pDesc', 'plmg', 'publisher',
                 'pubTime',
                 'descpic', 'isHot']
        list = ['pName', 'cld', 'pSn', 'PDesc']
        for i in list:
            if i == 'cld':
                kinds = tools.searchDB('kinds', ['id', 'kind'])
                for kind in kinds:
                    if name == str(kind[1]):
                        get = tools.searchDB(tableName='item', columns=[], where="cld ='" + str(kind[0]) + "'")
                        for ges in get:
                            for it in range(0, len(list0)):
                                dict[list0[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)
            else:
                data = tools.searchDB('item', columns=[], where=str(i) + " like'%" + str(name) + "%'")
                if data != ():
                    for ges in data:
                        dict = {}
                        for it in range(0, len(list0)):
                            dict[list0[it]] = str(ges[it])
                        if dict not in list1:
                            list1.append(dict)
        result['data'] = list1
        self.write(escape.json_decode(json.dumps(result)))



class RegisterWeb(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username")
        password1 = self.get_argument("password1")
        password2 = self.get_argument("password2")
        email = self.get_argument("email")
        if(username!="" and password1!= "" and password2!="" and email!=""):
            name = tools.searchDB('users',['username'],where="username = '"+username+"'")
            if name == ():
                max = tools.searchDB('users',['max(id)'])[0][0]
                if max == None:
                    max1 = 0
                else:
                    max1 = max
                today = datetime.date.today()
                listOfvalues = [str(max1+1),username, password1, password2,str(None),str(None),str(today)]
                listOfColumns = ['id', 'username', 'password', 'email', 'phonenum','address','regtime']
                if password1==password2 :
                    tools.insertDB('users',listOfColumns,listOfvalues)
                    result = {"state":"true","text":"注册成功"}
                else:
                    result = {"state":"false","text":"两次密码不一致"}
            else:
                result = {"state": "false", "text": "用户名已经被注册"}

        else:
            result={"state":"false","text":"请填完整信息"}
        self.write(escape.json_decode(json.dumps(result)))

class FilterWeb(tornado.web.RequestHandler):
    def get(self):
        # SELECT
        # pName, writer, iprice, plmg, item.id, pubTime
        # from item, kinds
        # where
        # kinds.kind = "小说" and item.cld = kinds.id and 20 <= iprice <= 50

        # 关键字
        name = self.get_argument("itemid")
        # 书的类型
        vary =  self.get_argument("find")
        # 排序方式
        sort = self.get_argument("sort")
        minprice = self.get_argument("minprice")
        maxprice = self.get_argument("maxprice")

        result = {}
        list0_1 = ['itemid', 'name', 'author', 'iPrice', 'plmg', 'pubTime']
        list1 = []
        if vary == "":
            list0 = ['id', 'pName', 'writer', 'iPrice', 'plmg', 'pubTime']
            list = ['pName', 'cld', 'pSn', 'PDesc']
            for i in list:
                if i == 'cld':
                    sql = "SELECT item.id, pName, writer, iPrice, plmg, pubTime from item, kinds where kinds.kind = '" + str(
                        name) + " 'and item.cld = kinds.id and " + str(minprice) + "<iPrice<" + str(maxprice)
                    get = tools.searchDB(sql=sql)
                    for ges in get:
                        dict = {}
                        for it in range(0, len(list0)):
                            dict[list0_1[it]] = str(ges[it])
                        list1.append(dict)
                elif i == 'pName':
                    data = tools.searchDB('item', columns=list0,
                                          where=str(i) + " like'%" + str(name) + "%'" + "and " + str(
                                              minprice) + "<iPrice<" + str(maxprice))
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0)):
                                dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)
                else:
                    data = tools.searchDB('item', columns=list0,
                                          where=str(i) + " ='" + str(name) + "'and " + str(minprice) + "<iPrice<" + str(
                                              maxprice))
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0)):
                                dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)

        else:
            k = ['pName', 'PDec']
            if name!='':
                for i in k:
                    sql = "SELECT pName, writer, iPrice, plmg, item.id, pubTime from item, kinds where kinds.kind = '" + str(
                        vary) + " 'and item.cld = kinds.id and " + str(minprice) + "<iPrice<" + str(maxprice) + "and" + str(
                        i) + " like'%" + str(name) + "%'"
                    data = tools.searchDB(sql=sql)
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0_1)):
                                dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)
            else:
                sql = "SELECT pName, writer, iPrice, plmg, item.id, pubTime from item, kinds where kinds.kind = '" + str(
                    vary) + " 'and item.cld = kinds.id and " + str(minprice) + "<iPrice<" + str(maxprice)
                data = tools.searchDB(sql=sql)
                if data != ():
                    for ges in data:
                        dict = {}
                        for it in range(0, len(list0_1)):
                            dict[list0_1[it]] = str(ges[it])
                        if dict not in list1:
                            list1.append(dict)
        if sort == '0':
            result['data'] = list1
        elif sort == '3':
            result['data'] = sorted(list1, key=lambda list1: list1['iPrice'])
        elif sort == '4':
            result['data'] = sorted(list1, key=lambda list1: list1['iPrice'], reverse=True)
        elif sort == '1':
            result['data'] = sorted(list1, key=lambda list1: list1['pubTime'])
        elif sort == '2':
            result['data'] = sorted(list1, key=lambda list1: list1['pubTime'], reverse=True)
        self.write(escape.json_decode(json.dumps(result)))

class ItemsWeb(tornado.web.RequestHandler):
    def get(self):
        id = self.get_argument("itemid")
        result = {'data': {}}
        sqlresult = tools.searchDB('item',
                                   ['pName', 'pSn', 'cld', 'mPrice', 'iPrice', 'writer', 'publisher', 'pubTime', 'plmg',
                                    'descpic', 'pDesc'], where="id='" + str(id) + "'")
        if sqlresult != ():
            result['state'] = 'success'
            result['itemname']=str(sqlresult[0][0])
            result['data']['itemname'] = str(sqlresult[0][0])
            result['data']['itemid'] = str(sqlresult[0][1])
            result['data']['itemcategory'] = str(tools.searchDB('kinds', ['kind'], where="id=" + str(sqlresult[0][2]))[0][0])
            result['data']['mprice'] = str(sqlresult[0][3])
            result['data']['iprice'] = str(sqlresult[0][4])
            result['data']['author'] = str(sqlresult[0][5])
            result['data']['publisher'] = str(sqlresult[0][6])
            result['data']['pubTime'] = str(sqlresult[0][7])
            result['data']['itempic'] = str(sqlresult[0][8])
            result['data']['descpic'] = str(sqlresult[0][9])
            result['data']['description'] = str(sqlresult[0][10])
        else:
            result['state'] = 'fail'
        self.write(escape.json_decode(json.dumps(result)))
#
# class addorder(tornado.web.RequestHandler):
#