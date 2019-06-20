class Router():
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # from .(foldername).(classname) import (classname)
        # app.register_blueprint(classname.api.blueprint)