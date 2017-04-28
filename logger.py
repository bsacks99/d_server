import logging
from logging.handlers import SysLogHandler

class Logger():

    __logger = None

    def __init__(self, config=None):
        self.__logger = logging.getLogger(config['environment'])
        self.__logger.setLevel(config['logging']['level'].upper())
        ch = logging.StreamHandler()
        ch.setLevel(config['logging']['level'].upper())

        self.__logger.addHandler(self.__get_handler(config))

    def __get_handler(self, config):

        ch = None
        if config['logging']['logger'] == 'stdout':
            ch = logging.StreamHandler()

        if config['logging']['logger'] == 'syslog':
            ch = SysLogHandler(address='/dev/log', facility=SysLogHandler.LOG_USER)
            formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
            ch.setFormatter(formatter)
        return ch

    def get_logger(self):
        return self.__logger