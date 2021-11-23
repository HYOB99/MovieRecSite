from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #specifying the relative path to the current file
db = SQLAlchemy(app)

from movierecsite import routes