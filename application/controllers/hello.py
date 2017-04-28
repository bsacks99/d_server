
from flask.views import MethodView
from flask import jsonify

class Hello(MethodView):

    def get(self):

        return jsonify({'hello': True})