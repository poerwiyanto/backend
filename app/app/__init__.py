from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')

# Define the database object.
db = SQLAlchemy(app)


# Import model(s).
from app.mod_tax.model import *

# Import module(s).
from app.mod_tax.controller import mod_tax

# Register blueprint(s).
app.register_blueprint(mod_tax)
