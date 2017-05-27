# -*- coding: utf-8 -*-
import tornado.web
from tornado import escape
import json
import tools
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class LoginWEB(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if (username != "" and password != ""):
            name = tools.searchDB('user', ['username'], where="username = '" + username + "'")
            email = tools.searchDB('user', ['email'], where="username = '" + username + "'")
            if name!= () or email!=():
                if username == name[0][0].decode('utf-8') or username == email[0][0]:
                    password_0 = tools.searchDB('user', ['password'], where="password = '" + password + "'")
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
		
class move(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("information")
        print username
        if username=="123":
            result = {"state":"true"}
            print 'ok'
        else:
            result = {"state":"false"}
        self.write(escape.json_decode(json.dumps(result)))
		
class Registerweb(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("username")
        password1 = self.get_argument("password1")
        password2 = self.get_argument("password2")
        email = self.get_argument("email")
        if(username!="" and password1!= "" and password2!="" and email!=""):
            name = tools.searchDB('user',['username'],where="username = '"+username+"'")
            if name == ():
                listOfColumns =['id', 'username', 'password','email']
                lens = tools.searchDB('user',['count(id)'])[0][0]
                print lens
                if password1==password2 :
                    listOfvalues = [str(lens+1),username,password1,password2]
                    tools.insertDB('user',listOfColumns,listOfvalues)
                    result = {"state":"true","text":"注册成功"}
                else:
                    result = {"state":"false","text":"两次密码不一致"}
            else:
                result = {"state": "false", "text": "用户名已经被注册"}

        else:
            result={"state":"false","text":"请填完整信息"}
        print result
        self.write(escape.json_decode(json.dumps(result)))

class filter(tornado.web.RequestHandler):
    def get(self):
        username = self.get_argument("information")
        print username
        if username=="123":
            result = {"state":"true"}
            print 'ok'
        else:
            result = {"state":"false"}
        self.write(escape.json_decode(json.dumps(result)))