import json

class Config():

    __env = 'development'
    __config_file = '_app.json'
    __config = None

    def __init__(self, env=None):
        if env is not None:
            self.__env = env

        self.__config_file = "config/{0}{1}".format(self.__env, self.__config_file)

        self.__set_config()

    def __set_config(self):

        try:
            with open(self.__config_file) as data_file:    
                self.__config = json.load(data_file)
        except Exception as e:
            print("ERROR: {}".format(e))
            raise(e)

    def get_config(self):
        return self.__config