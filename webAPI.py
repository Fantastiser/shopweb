# -*- coding: utf-8 -*-
import tornado.web
from tornado import escape
import json
import datetime
import tools
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class LogoutHandler(BaseHandler):
    def post(self):
        if (self.get_argument("logout")!=None):
            self.clear_cookie("user")
            self.current_user = "[登录]"
        result = {"state": "true", "text": "退出登录成功"}
        self.write(escape.json_decode(json.dumps(result)))
class LoginWeb(BaseHandler):
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
                        self.set_secure_cookie("user", username,expires_days = None)
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
                listOfvalues = [str(max1+1),username, password1, email,str(None),str(None),str(None),str(today)]
                listOfColumns = ['id', 'username', 'password', 'email', 'phonenum','receiver','address','regtime']
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
        if vary == "null":
            list0 = ['id', 'pName', 'writer', 'iPrice', 'plmg', 'pubTime']
            list = ['pName', 'cld', 'pSn', 'PDesc']
            for i in list:
                if i == 'cld':
                    sql = "SELECT item.id, pName, writer, iPrice, plmg, pubTime from item, kinds where kinds.kind = '" + str(
                        name) + " 'and item.cld = kinds.id and " + str(minprice) + "<=iPrice and iPrice<="+str(maxprice)
                    get = tools.searchDB(sql=sql)
                    for ges in get:
                        dict = {}
                        for it in range(0, len(list0)):
                            if list0_1[it] == "iPrice":
                                dict[list0_1[it]] = float(ges[it])
                            else:
                                dict[list0_1[it]] = str(ges[it])
                        list1.append(dict)
                elif i == 'pName':
                    data = tools.searchDB('item', columns=list0,
                                          where=str(i) + " like'%" + str(name) + "%'" + "and " + str(minprice) + "<=iPrice and iPrice<="+str(maxprice))
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0)):
                                if list0_1[it] == "iPrice":
                                    dict[list0_1[it]] = float(ges[it])
                                else:
                                    dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)
                else:
                    data = tools.searchDB('item', columns=list0,
                                          where=str(i) + " ='" + str(name) + "'and " +str(minprice) + "<=iPrice and iPrice<="+str(maxprice))
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0)):
                                if list0_1[it] == "iPrice":
                                    dict[list0_1[it]] = float(ges[it])
                                else:
                                    dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)

        else:
            k = ['pName', 'PDesc']
            if name != '':
                for i in k:
                    sql = "SELECT item.id, pName, writer, iPrice, plmg, pubTime from item, kinds where kinds.kind = '{0} 'and item.cld = kinds.id and {1}<=iPrice and iPrice<= {2} and {3} like'%{4}%'".format(
                        str(vary), str(minprice), str(maxprice), str(i), str(name))
                    data = tools.searchDB(sql=sql.decode('utf8'))
                    if data != ():
                        for ges in data:
                            dict = {}
                            for it in range(0, len(list0_1)):
                                if list0_1[it] == "iPrice":
                                    dict[list0_1[it]] = float(ges[it])
                                else:
                                    dict[list0_1[it]] = str(ges[it])
                            if dict not in list1:
                                list1.append(dict)
            else:
                sql = "SELECT item.id, pName, writer, iPrice, plmg, pubTime from item, kinds where kinds.kind = '" + str(
                    vary) + " 'and item.cld = kinds.id and " + str(minprice) + "<=iPrice and iPrice<="+str(maxprice)

                data = tools.searchDB(sql=sql)
                if data != ():
                    for ges in data:
                        dict = {}
                        for it in range(0, len(list0_1)):
                            if list0_1[it] =="iPrice":
                                dict[list0_1[it]] = int(ges[it])
                            else:
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
            result['data']['pubdate'] = str(sqlresult[0][7])
            result['data']['itempic'] = str(sqlresult[0][8])
            result['data']['descpic'] = str(sqlresult[0][9])
            result['data']['description'] = str(sqlresult[0][10])
        else:
            result['state'] = 'fail'
        self.write(escape.json_decode(json.dumps(result)))


class shopcartnum(tornado.web.RequestHandler):
    def get(self):
        result={}
        username =  self.get_argument("username")
        num = tools.searchDB('orders',['username'],where = "username='{0}' and conditions={1}".format(username,str('0')))
        if num!=():
            result['num'] =len(num)
        else:
            result['num'] = 0
        self.write(escape.json_decode(json.dumps(result)))

class addorder(tornado.web.RequestHandler):
    def get(self):
        result={}
        itemid = self.get_argument("itemid")
        name = self.get_argument("itemname")
        user = self.get_argument("user")
        num = self.get_argument("num")
        regtime = datetime.date.today()
        price = self.get_argument("price")
        condition = self.get_argument("condition")
        amount = float(num)*float(price)
        number = tools.searchDB('orders',['num'],where = "itemid='{0}' and username ='{1}' and conditions ='{2}'".format(str(itemid),str(user),str(condition)))
        if str(condition)=="1":
            sql0 = "delete from orders  where conditions='{1}'and username='{0}'".format(str(name), '1')
            tools.insertDB(sql=sql0)
        if number==():
            max = tools.searchDB('orders', ['max(id)'])[0][0]
            if max == None:
                max1 = 0
            else:
                max1 = max
            sql = "insert  into orders (id,itemid,itemname,username,receiver,tel,address,num,regtime,price,amount,conditions) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(str(int(max1)+1),str(itemid),str(name),str(user),str("None"),str("None"),str("None"),str(num),str(regtime),str(price),str(amount),str(condition))
            tools.insertDB(sql=sql)
        else:
            nums=int(number[0][0])+int(num)
            amount = float(nums)*float(price)
            sql = "UPDATE orders SET amount= '{0}',num='{1}'".format(str(amount),str(nums))+" where itemid ='{0}' and username='{1}' and conditions='{2}'".format(str(itemid),str(user),str(condition))
            tools.insertDB(sql = sql)
        result["msg"]="true"
        self.write(escape.json_decode(json.dumps(result)))

class checkorder(tornado.web.RequestHandler):
    def get(self):
        list1=[]
        name = self.get_argument("username")
        condition = self.get_argument("condition")
        if str(condition)=="3":
            sql = "SELECT receiver,address,phonenum from users where users.username ='{0}'".format( str(name))
            data1 = tools.searchDB(sql=sql)
            if data1!=():
                datas = data1[0]
                receiver = datas[0]
                address = datas[1]
                phonenum = datas[2]
                if str(datas[0]) == "None":
                    receiver =""
                if str(datas[1]) == "None":
                    address = ""
                if str(datas[2]) == "None":
                    phonenum = ""
                user = { "receiver": receiver, "address": address, "tel": phonenum}
                list0 = ["pic", "name", "info", "stdprice", "price", "number", "amount", "id","status","ordernum"]
                datas = tools.searchDB(
                    sql="SELECT plmg,pName,writer,mPrice,iPrice,num,amount,item.id,conditions,orders.id from orders,item where orders.itemid =item.id and username= '{0}' and conditions != '{1}'".format(
                        str(name), str(0)))

                for data in datas:
                    dict = {}
                    for i in xrange(0, len(list0)):
                        if list0[i] =="status":
                            if str(data[i])=='1':
                                dict[list0[i]] = "待下单"
                            elif str(data[i])=='2':
                                dict[list0[i]] = "已付款"
                            elif str(data[i]) == '3':
                                dict[list0[i]] = "已发货"
                            elif str(data[i]) == '4':
                                dict[list0[i]] = "已完成"
                        else:
                            dict[list0[i]] = str(data[i])
                    list1.append(dict)
                result = {"msg":"success","data": list1,"user":user}
            else:
                result ={"msg":"fail"}
        else:
            sql = "SELECT phonenum from users where username ='{0}'".format(str(name))
            data1 = tools.searchDB(sql=sql)
            if data1 != ():
                list0 = ["pic", "name", "info", "stdprice", "price", "number", "amount", "id"]
                datas = tools.searchDB(
                    sql="SELECT plmg,pName,writer,mPrice,iPrice,num,amount,item.id from orders,item where orders.itemid =item.id and username= '{0}' and conditions = '{1}'".format(
                        str(name), str(condition)))

                for data in datas:
                    dict = {}
                    for i in xrange(0, len(list0)):
                        dict[list0[i]] = str(data[i])
                    list1.append(dict)
                result = {"data": list1}
                result["msg"] = "success"
                if str(condition)=='1':
                    sql="SELECT users.username,users.receiver,users.address,phonenum from users,orders where users.username = orders.username and conditions ='{0}' and users.username ='{1}'".format(str(condition),str(name))

                    data1 = tools.searchDB(sql = sql)
                    if data1 != ():
                        datas = data1[0]
                        receiver = datas[1]
                        address = datas[2]
                        phonenum = datas[3]
                        if str(datas[0]) == "None":
                            receiver = ""
                        if str(datas[1]) == "None":
                            address = ""
                        if str(datas[2]) == "None":
                            phonenum = ""
                        result["user"] = {"username": str(datas[0]), "receiver": receiver, "address": address,
                                          "tel": phonenum}
                        result["msg"] = "success"
            else:
                result = {"msg" :"fail"}
        self.write(escape.json_decode(json.dumps(result)))

class changeorder(tornado.web.RequestHandler):
    def get(self):
        result={}
        name = self.get_argument("username")
        id0 = self.get_argument("id")
        id = id0.split(';')
        condition = self.get_argument("condition")
        if str(condition) =='0':
            try:
                for i in id:
                    tools.deleteDB('orders',where="username='{0}' and conditions='{1}' and itemid = '{2}'".format(str(name),str(condition),str(i)))
                result = {"data":"true"}
            except:
                result = {"data": "false"}
        elif(str(condition)=='1'):
            try:
                sql0 = "delete from orders  where conditions='{1}'and username='{0}'".format(str(name),'1')
                tools.insertDB(sql=sql0)
                for i in id:
                    sql = "UPDATE orders SET conditions='{0}' where itemid ='{1}'and username='{2}'".format(str(condition),
                                                                                                            str(i),
                                                                                                       str(name))
                    tools.insertDB(sql = sql)
                result = {"data": "true"}
            except:
                result = {"data": "false"}

        self.write(escape.json_decode(json.dumps(result)))
class commit(tornado.web.RequestHandler):
    def get(self):
        result = {}
        name = self.get_argument("username")
        condition = self.get_argument("condition")
        if (str(condition) == '2'):
            try:
                answer = tools.searchDB('users', ['receiver', 'phonenum', 'address'],
                                        where="username ='{0}'".format(str(name)))
                id = tools.searchDB('orders', ['itemid','num'],
                                        where="conditions ='{0}'and username='{1}'".format("1",str(name)))
                for i in id:
                    sql0 = "UPDATE item SET isHot=isHot+'{0}' where id ='{1}'".format(str(i[1]),str(i[0]))
                    tools.insertDB(sql = sql0)
                sql = "UPDATE orders SET conditions='{0}',receiver='{3}',tel='{4}',address ='{5}'  where conditions ='{1}'and username='{2}'".format(
                    str(condition),
                    "1",
                    str(name), str(answer[0][0]), str(answer[0][1]), str(answer[0][2]))
                tools.insertDB(sql=sql)

                result = {"data": "2", "text": "支付成功"}
            except:
                result = {"data": "false"}

        elif(str(condition) == '1'):
            try:
                sql0 = "UPDATE orders SET conditions='{0}' where username='{1}'".format('0', str(name))
                tools.insertDB(sql=sql0)
                result = {"data": "1", "text": "取消订单成功"}
            except:
                result = {"data": "false"}
        self.write(escape.json_decode(json.dumps(result)))


class changeaddress(tornado.web.RequestHandler):
    def get(self):
        result={}
        username = self.get_argument("username")
        receiver = self.get_argument("receiver")
        tel = self.get_argument("tel")
        address = self.get_argument("address")
        regtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sql = "UPDATE users SET receiver= '{0}',phonenum='{1}',address='{2}'".format(str(receiver),str(tel),str(address))+" where username='{0}'".format(str(username))
        tools.insertDB(sql = sql)
        sql1 = "UPDATE orders SET regtime= '{0}'".format(str(regtime)) + " where username='{0}'".format(str(username))
        tools.insertDB(sql=sql1)
        result["msg"]="true"
        self.write(escape.json_decode(json.dumps(result)))