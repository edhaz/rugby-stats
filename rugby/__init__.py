from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rugby.settings import SECRET_KEY, DATABASE_PATH

app = Flask(__name__)
app.secret_key = SECRET_KEY if SECRET_KEY else "development"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + DATABASE_PATH
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


from rugby import routes, models  # noqa: E402, F401
