import os
import tornado.web
from views import Start,Shops,Login,Register,Filter
from webAPI import LoginWeb,move,RegisterWeb,FilterWeb
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SETTINGS = {
    "template_path": os.path.join(BASE_DIR, "templates"),
    "static_path": os.path.join(BASE_DIR, "static")
}

HANDLERS = [
    (r"/", Start),
    (r"/login", Login),
    (r"/ajax/login", LoginWeb),
	(r"/shop", Start),
	(r"/ajax/shop", move),
	(r"/register",Register),
	(r"/ajax/register",RegisterWeb),
    (r"/filter",Filter),
    (r"/ajax/filter",FilterWeb),
]

UI_MODULES={
	'Shop': Shops
}

application = tornado.web.Application(
    handlers = HANDLERS,
    ui_modules=UI_MODULES,
**SETTINGS)
