
import importlib
from routes import Routes

class Bootstrap():
    __app = None
    __config = None
    __logger = None

    def __init__(self):
        pass

    def set_logger(self, logger):
        self.__logger = logger
        self.__logger.info("logger has been set.")

    def set_app(self, app):
        self.__logger.info("setting app.")
        self.__app = app

    def set_config(self, config):
        self.__logger.info("setting config.")
        self.__config = config

    def set_up_routes(self):
        rt = Routes()
        routes = rt.get_routes()
        for route in routes:
            self.__logger.info("setting up route: {}".format(route))
            module = importlib.import_module("application.controllers.{}".format(route))
            class_ = getattr(module, route.title())

            class_args = []
            class_kwargs = {
                'logger': self.__logger,
                'config': self.__config
            }

            for rule in routes[route]:
                self.__logger.info("setting up enpoint: {}".format(rule))
                self.__app.add_url_rule(rule, view_func=class_.as_view(rule, *class_args, **class_kwargs))

    def go(self):
        self.__logger.info("running app.")
        self.__app.run()