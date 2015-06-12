from tornado.ioloop import IOLoop
from tornado.web import Application
from app import app
from app.kernel import kernel

def main():
    router = kernel.single('base_router').router()
    app = Application(router, settings={"debug": True})
    app.listen(8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
