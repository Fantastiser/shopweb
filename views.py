# -*- coding: utf-8 -*-
import tornado.web

class Start(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',
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

class HeaderModule(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "header.html"
        )
        
    def css_files(self):
        return "/static/css/xgxt_login.css"

class LoginModule(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "login.html",
        )
        
    def javascript_files(self):
        return ["/static/js/test.js","/static/js/jquery.js"]
		
class Shops(tornado.web.UIModule):
    def render(self):
        return self.render_string(
            "index.html",
        )
        
    def javascript_files(self):
        return ["/static/js/DD_belatedPNG_0.0.8a-min.js","/static/js/ie6Fixpng.js","/static/js/test.js"]

