import config
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
app = flask.Flask("Lilm")
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQL_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socket = SocketIO(app)