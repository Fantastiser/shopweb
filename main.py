import tornado.ioloop
from tornado.options import define, options
import socket 
from urls import application

define("port", default=8000, help="run on the given port", type=int)
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
application.listen(options.port)
print "Starting development server at http://"+str(myaddr)+":"+str(options.port)
tornado.ioloop.IOLoop.instance().start()
