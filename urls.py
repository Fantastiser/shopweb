import os
import tornado.web
from views import Start,HelloModule,Login,Register,Filter,Item,Shopcart,checkorders
from webAPI import LoginWeb,Move,RegisterWeb,FilterWeb,ItemsWeb,shopcartnum,addorder,LogoutHandler,checkorder,changeorder,changeaddress
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static"),
"cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
}
class PageNotFoundHandler(tornado.web.RequestHandler):
    def get(self):
        return self.write_error(404)
HANDLERS = [
    (r"/", tornado.web.RedirectHandler, {"url": "/shop"}),
    (r"/login", Login),
	(r"/shop", Start),
    (r"/filter",Filter),
    (r"/register",Register),
    (r"/items",Item),
    (r"/shopcart",Shopcart),
    (r"/checkorder",checkorders),
	(r"/ajax/shop", Move),
    (r"/ajax/login", LoginWeb),
    (r'/ajax/logout', LogoutHandler),
	(r"/ajax/register",RegisterWeb),
    (r"/ajax/filter",FilterWeb),
    (r"/ajax/items",ItemsWeb),
    (r"/ajax/shopcartnum",shopcartnum),
    (r"/ajax/addorder",addorder),
    (r"/ajax/checkorder",checkorder),
(r"/ajax/changeorder",changeorder),
(r"/ajax/changeaddress",changeaddress),
    (r".*", PageNotFoundHandler),
]

UI_MODULES={
	'Hello':HelloModule
}

application = tornado.web.Application(
    handlers = HANDLERS,
    ui_modules=UI_MODULES,
**SETTINGS)
