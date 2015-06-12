from tornado.ioloop import IOLoop
from tornado.web import Application
from config.config import config

class kernel:
    __singleton_instance = {}
    
    @staticmethod
    def boot():
        router = kernel.single('base_router').router()
        webapp = Application(router, settings={"debug": config.debug})
        webapp.listen(config.http_port)
        IOLoop.current().start()
    
    @staticmethod
    def single(classname):
        p = classname.index('_')
        if p:
            appname = classname[:p]
            classmodule = classname[p+1:]
            type = classmodule[:3]
            if type == 'ctl':
                classmodule = classmodule[4:].replace('_', '.')
                mvc = 'controller'
            elif type == 'mdl':
                classmodule = classmodule[4:].replace('_', '.')
                mvc = 'model'
            else:
                classmodule = classmodule.replace('_', '.')
                mvc = 'lib'
            path = config.app_dir+'.'+appname+'.'+mvc+'.'+classmodule
            if classname not in kernel.__singleton_instance:
                kernel.__singleton_instance[classname] = __import__(path).__getattribute__(appname).__getattribute__(mvc).__getattribute__(classmodule).__getattribute__(classname)
            return kernel.__singleton_instance[classname]
        return None
