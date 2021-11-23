from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #specifying the relative path to the current file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in_page'

from movierecsite import routes