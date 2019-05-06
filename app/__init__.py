from flask import Flask
from flask_moment import Moment
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
moment = Moment(app)

from app import routes, models
