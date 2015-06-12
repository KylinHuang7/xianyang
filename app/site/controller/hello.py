import tornado

class site_ctl_hello(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
