class kernel:
    @staticmethod
    def boot():
        pass
    
    @staticmethod
    def single(classname):
        p = classname.index('_')
        APP_DIR = 'app'
        if p:
            app = classname[:p]
            classmodule = classname[p+1:]
            type = classmodule[:3]
            if type == 'ctl':
                classmodule = classmodule[4:].replace('_', '.')
                path = APP_DIR+'.'+app+'.controller.'+classmodule
                return __import__(path).__getattribute__(app).__getattribute__('controller').__getattribute__(classmodule).__getattribute__(classname)
            elif type == 'mdl':
                classmodule = classmodule[4:].replace('_', '.')
                path = APP_DIR+'.'+app+'.model.'+classmodule
                return __import__(path).__getattribute__(app).__getattribute__('model').__getattribute__(classmodule).__getattribute__(classname)
            else:
                classmodule = classmodule[1:].replace('_', '.')
                path = APP_DIR+'.'+app+'.lib.'+classmodule
                return __import__(path).__getattribute__(app).__getattribute__('lib').__getattribute__(classmodule).__getattribute__(classname)
        return None
