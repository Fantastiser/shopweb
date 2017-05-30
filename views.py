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
        theme1 = tools.searchDB(sql='select pName,mPrice,iPrice,plmg ,id from item where cld = {0} ORDER BY isHot DESC '.format(str(a)))
        theme2 = tools.searchDB(sql='select pName,mPrice,iPrice,plmg ,id from item where cld = {0} ORDER BY isHot DESC '.format(str(b)))
        pic_url = tools.searchDB(sql='select itemid,albumpath from album ')
        pic_ul = random.sample(pic_url, 4)
        self.render('index.html',
            pic_url1= pic_ul[0][1],
            pic_url2 = pic_ul[1][1],
            pic_url3=pic_ul[2][1],
            pic_url4=pic_ul[3][1],
            titlename1=titlename1,
            background1 = '../static/images/goods/mi6.jpg',
            part1_src1=theme1[0][3],
            part1_name1 = theme1[0][0],
            part1_iprice1 =theme1[0][2],
            part1_mprice1 =theme1[0][1],
            part1_namesrc1= theme1[0][4],
            part1_namesrc2=theme1[1][4],
            part1_namesrc3=theme1[2][4],
            part1_namesrc4=theme1[3][4],
            part2_namesrc1=theme2[0][4],
            part2_namesrc2=theme2[1][4],
            part2_namesrc3=theme2[2][4],
            part2_namesrc4=theme2[3][4],
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
class Item(tornado.web.RequestHandler):
    def get(self):
        self.render('items.html',
		)
class HelloModule(tornado.web.UIModule):
    def render(self):
        list = []
        list1 = []
        list2 = []
        for i in range(1, 11):
            kind = tools.searchDB('kinds', ['kind'], where="id = '" + str(i) + "'")[0][0]
            list.append(kind)
            item = tools.searchDB(sql='select pName,id from item where cld = {0} ORDER BY isHot DESC '.format(str(i)))
            if item != ():
                list1.append(item[0][1])
                list2.append(item[0][0])
        return '''<dl class="shopClass_item">
            				<dt><a id="varity1"  title={0} href="#" class="b" >{0}</a> <a id="varity2"  title={1} href="#" class="b">{1}</a></dt>
            						<dd><a id="good1" title={2} href="{20}" >{2}</a> <a id="good2" title={3} href="{21}">{3}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a id="varity3" title={4} href="#" class="b">{4}</a> <a id="varity4" title={5} href="#" class="b">{5}</a></dt>
            						<dd><a id="good3" title={6} href="{22}">{6}</a> <a id="good4" title={7} href="{23}">{7}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a id="varity5" title={8} href="#" class="b">{8}</a> <a id="varity6" title={9} href="#" class="b">{9}</a></dt>
            						<dd><a id="good5" title={10} href="{24}">{10}</a> <a id="good6" title={11} href="{25}">{11}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a id="varity7" title={12} href="#" class="b">{12}</a> <a id="varity8" title={13} href="#" class="b">{13}</a></dt>
            						<dd><a id="good7" title={14} href="{26}">{14}</a> <a id="good8" title={15} href="{27}">{15}</a> </dd>
            					</dl>
            					<dl class="shopClass_item">
            				<dt><a id="varity9" title={16} href="#" class="b">{16}</a> <a id="varity10" title={17} href="#" class="b">{17}</a></dt>
            						<dd><a title={18} id="good9" href="{28}">{18}</a> <a id="good10" title={19} href="{29}">{19}</a> </dd>
            					</dl>'''.format(list[0], list[1], list2[0], list2[1], list[2], list[3], list2[2],
                                                list2[3], list[4], list[5], list2[4], list2[5], list[6], list[7],
                                                list2[6], list2[7], list[8], list[9], list2[8], list2[9],list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6],list1[7],list1[8],list1[9])




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

