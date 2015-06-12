from app.kernel import kernel

class base_router:
    @staticmethod
    def router():
        return [
            (r"/", kernel.single('site_ctl_hello')), 
        ]
