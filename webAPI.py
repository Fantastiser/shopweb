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
                listOfvalues = [str(max1+1),username, password1, password2,str(today),str(None),str(None)]
                listOfColumns = ['id', 'username', 'password', 'email', 'regtime','address','shopcart']
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
        name = self.get_argument("information")
        result = {}
        dict = {}
        list1 = []
        list0 = ['id', 'pName', 'pSn', 'cld', 'pNum', 'mPrice', 'iPrice', 'pDesc', 'plmg', 'pubTime', 'ishow', 'isHot']
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
                        for it in range(0, len(list0)):
                            dict[list0[it]] = str(ges[it])
                        if dict not in list1:
                            list1.append(dict)
        result['data'] = list1
        self.write(escape.json_decode(json.dumps(result)))