from flask import Flask, jsonify
from flask_classful import FlaskView


def start(config = None):
    app = Flask(__name__)
    
    # See http://flask.pocoo.org/docs/latest/config/
    app.config.update(dict(DEBUG=True))
    app.config.update(config or {})
    
    FaceView.register(app)

    app.run(host = '0.0.0.0', port = 8082)

class FaceView(FlaskView):
    route_prefix = 'proto'
    route_base = 'face'
    default_methods = ['GET']

    def happy(self):
        return "Hewwo x3"

    def sad(self):
        return "Bleh......."

    def angory(self):
        return "Fuck off ya fucken wanker!!!!!!!"