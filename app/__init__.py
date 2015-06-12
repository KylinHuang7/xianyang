from app.kernel import kernel

class app:
    __instance = {}
    
    def __init__(self, app_id):
        self.app_id = app_id
    
    @staticmethod
    def get(app_id):
        if app_id not in app.__instance:
            app.__instance[app_id] = app(app_id)
        return app.__instance[app_id]
    
    def controller(self, controller):
        return kernel.single(self.app_id+'_ctl_'+controller)
    
    def model(self, model):
        return kernel.single(self.app_id+'_mdl_'+model)
