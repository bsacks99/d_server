
class Routes():

    __routes = {
        'hello': [
            '/hello',
            '/hello/<uuid:object>'
        ]
    }

    def __init__(self):
        pass

    def get_routes(self):
        return self.__routes