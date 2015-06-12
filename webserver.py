from tornado.ioloop import IOLoop
from tornado.web import Application
from app.kernel import kernel

def make_app():
    return Application([
        (r"/", kernel.single('site_ctl_hello')), 
    ], settings={"debug": True})

def main():
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
