from flask import request
from application.core.controller import Controller

class Hello(Controller):

    def __init__(self, *args, **kwargs):
        print(kwargs)
        exit
        super().__init__(**kwargs)

    def get_handler(self, object=None):

        data = {'hello': True}

        return self.get_response(data)

    def post_handler(self, object=None):

        print(request.data)

        data = {'hello': True}

        return self.get_response(data)