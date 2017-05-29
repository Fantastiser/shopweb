# -*- coding: utf-8 -*-
import tornado.web
import tools
import random
class Start(tornado.web.RequestHandler):
    def get(self):
        a = random.randint(1, 10)
        if a > 5:
            b = random.randint(1, a - 1)
        else:
            b = random.randint(a + 1, 10)
        titlename1= tools.searchDB('kinds', ['kind'], where="id = '" + str(a) + "'")[0][0]
        titlename2 = tools.searchDB('kinds', ['kind'], where="id = '" + str(b) + "'")[0][0]
        theme1 = tools.searchDB(sql='select pName,mPrice,iPrice,plmg from item where cld = {0} ORDER BY isHot DESC '.format(str(a)))
        theme2 = tools.searchDB(sql='select pName,mPrice,iPrice,plmg from item where cld = {0} ORDER BY isHot DESC '.format(str(b)))
        pic_url = tools.searchDB(sql='select itemid,albumpath from album  ')
        self.render('index.html',
            url1='',
            url2='',
            url3='',
            url4='',
            pic_url1=,
            pic_url2 = ,
            pic_url3=,
            pic_url4=,
            titlename1=titlename1,
            background1 = '../static/images/goods/mi6.jpg',
            part1_src1=theme1[0][3],
            part1_name1 = theme1[0][0],
            part1_iprice1 =theme1[0][2],
            part1_mprice1 =theme1[0][1],
            part1_src2=theme1[1][3],
            part1_name2=theme1[1][0],
            part1_iprice2=theme1[1][2],
            part1_mprice2=theme1[1][1],
            part1_src3=theme1[2][3],
            part1_name3=theme1[2][0],
            part1_iprice3=theme1[2][2],
            part1_mprice3=theme1[2][1],
            part1_src4=theme1[3][3],
            part1_name4=theme1[3][0],
            part1_iprice4=theme1[3][2],
            part1_mprice4=theme1[3][1],
            titlename2=titlename2,
            background2='../static/images/goods/mi6.jpg',
            part2_src1=theme2[0][3],
            part2_name1=theme2[0][0],
            part2_iprice1=theme2[0][2],
            part2_mprice1=theme2[0][1],
            part2_src2=theme2[1][3],
            part2_name2=theme2[1][0],
            part2_iprice2=theme2[1][2],
            part2_mprice2=theme2[1][1],
            part2_src3=theme2[2][3],
            part2_name3=theme2[2][0],
            part2_iprice3=theme2[2][2],
            part2_mprice3=theme2[2][1],
            part2_src4=theme2[3][3],
            part2_name4=theme2[3][0],
            part2_iprice4=theme2[3][2],
            part2_mprice4=theme2[3][1],
        )

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html',
		)

class Register(tornado.web.RequestHandler):
    def get(self):
        self.render('register.html',
		)

class Filter(tornado.web.RequestHandler):
    def get(self):
        self.render('filter.html',
		)

class HelloModule(tornado.web.UIModule):
    def render(self):
        list = []
        list2 = []
        for i in range(1, 11):
            kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
            list.append(kind)
            item = tools.searchDB('item', ['pName', 'min(isHot)'], where="cld = '" + str(i) + "'")
            if item != ():
                list2.append(item[0][0])
        return '''<dl class="shopClass_item">
            				<dt><a href="#" class="b">{0}</a> <a href="#" class="b">{1}</a></dt>
            						<dd><a href="#">{2}</a> <a href="#">{3}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a href="#" class="b">{4}</a> <a href="#" class="b">{5}</a></dt>
            						<dd><a href="#">{6}</a> <a href="#">{7}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a href="#" class="b">{8}</a> <a href="#" class="b">{9}</a></dt>
            						<dd><a href="#">{10}</a> <a href="#">{11}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a href="#" class="b">{12}</a> <a href="#" class="b">{13}</a></dt>
            						<dd><a href="#">{14}</a> <a href="#">{15}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a href="#" class="b">{16}</a> <a href="#" class="b">{17}</a></dt>
            						<dd><a href="#">{18}</a> <a href="#">{19}</a> </dd>
            					</dl>'''.format(list[0], list[1], list2[0], list2[1], list[2], list[3], list2[2],
                                                list2[3], list[4], list[5], list2[4], list2[5], list[6], list[7],
                                                list2[6], list2[7], list[8], list[9], list2[8], list2[9])
            # list = []
            # list2 = []
            # for i in range(1, 9):
            #     list0 = []
            #     kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
            #     list.append(kind)
            #     item = tools.searchDB('item', ['pName'], where="cld = '" + str(i) + "'")
            #     if item != ():
            #         for j in item:
            #             list0.append(j[0])
            #     list1 = sorted(set(list0), key=list0.index)
            #     list2.append(list1)
            # return'''<dl class="shopClass_item">
				# <dt><a href="#" class="b">{0}</a> <a href="#" class="b">{1}</a></dt>
				# 		<dd><a href="#">{2}</a> <a href="#">{3}</a> </dd>
				# 	</dl>
				# 	<dl class="shopClass_item">
				# <dt><a href="#" class="b">{4}</a> <a href="#" class="b">{5}</a></dt>
				# 		<dd><a href="#">{6}</a> <a href="#">{7}</a> </dd>
				# 	</dl>
				# 	<dl class="shopClass_item">
				# <dt><a href="#" class="b">{8}</a> <a href="#" class="b">{9}</a></dt>
				# 		<dd><a href="#">{10}</a> <a href="#">{11}</a> </dd>
				# 	</dl>
				# 	<dl class="shopClass_item">
				# <dt><a href="#" class="b">{12}</a> <a href="#" class="b">{13}</a></dt>
				# 		<dd><a href="#">{14}</a> <a href="#">{15}</a> </dd>
				# 	</dl>'''.format(list[0],list[1],list2[0][0],list2[1][0],list[2],list[3],list2[2][0],list2[3][0],list[4],list[5],list2[4][0],list2[5][0],list[6],list[7],list2[6][0],list2[7][0])



# class HeaderModule(tornado.web.UIModule):
#     def render(self):
#         return self.render_string(
#             "header.html"
#         )
#
#     def css_files(self):
#         return "/static/css/xgxt_login.css"
#
# class LoginModule(tornado.web.UIModule):
#     def render(self):
#         return self.render_string(
#             "login.html",
#         )
#
#     def javascript_files(self):
#         return ["/static/js/test.js","/static/js/jquery.js"]
#
# class Shops(tornado.web.UIModule):
#     def render(self):
#         return self.render_string(
#             "index.html",
#         )
#
#     def javascript_files(self):
#         return ["/static/js/DD_belatedPNG_0.0.8a-min.js","/static/js/ie6Fixpng.js","/static/js/test.js"]

