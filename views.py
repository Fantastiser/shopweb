# -*- coding: utf-8 -*-
import tornado.web
import tools
class Start(tornado.web.RequestHandler):
    def get(self):

        self.render('index.html',
            url1='../static/images/goods/air2.jpg',
            url2 = '../static/images/goods/shorts.jpg',
            url3='../static/images/goods/charqui.jpg',
            url4='../static/images/goods/mi6.jpg',
            titlename1='小说',
            background1 = '../static/images/goods/mi6.jpg',
            part1_src1='../static/images/goods/mi6.jpg',
            part1_name1 = '小米6',
            part1_iprice1 ='2000',
            part1_mprice1 ='2499',
            part1_src2='../static/images/goods/mi6.jpg',
            part1_name2='小米6',
            part1_iprice2='2000',
            part1_mprice2='2499',
            part1_src3='../static/images/goods/mi6.jpg',
            part1_name3='小米6',
            part1_iprice3='2000',
            part1_mprice3='2499',
            part1_src4='../static/images/goods/mi6.jpg',
            part1_name4='小米6',
            part1_iprice4='2000',
            part1_mprice4='2499',
            titlename2='电子书',
            background2='../static/images/goods/mi6.jpg',
            part2_src1='../static/images/goods/mi6.jpg',
            part2_name1='mate9',
            part2_iprice1='2000',
            part2_mprice1='2499',
            part2_src2='../static/images/goods/mi6.jpg',
            part2_name2='mate9',
            part2_iprice2='2000',
            part2_mprice2='2499',
            part2_src3='../static/images/goods/mi6.jpg',
            part2_name3='mate9',
            part2_iprice3='2000',
            part2_mprice3='2499',
            part2_src4='../static/images/goods/mi6.jpg',
            part2_name4='mate9',
            part2_iprice4='2000',
            part2_mprice4='2499',
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
            for i in range(1, 9):
                list0 = []
                kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
                list.append(kind)
                item = tools.searchDB('item', ['pName'], where="cld = '" + str(i) + "'")
                if item != ():
                    for j in item:
                        list0.append(j[0])
                list1 = sorted(set(list0), key=list0.index)
                list2.append(list1)
            return'''<dl class="shopClass_item">
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
					</dl>'''.format(list[0],list[1],list2[0][0],list2[1][0],list[2],list[3],list2[2][0],list2[3][0],list[4],list[5],list2[4][0],list2[5][0],list[6],list[7],list2[6][0],list2[7][0])



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

