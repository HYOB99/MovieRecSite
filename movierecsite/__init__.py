import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #specifying the relative path to the current file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'sign_in_page'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_ADD_PROJ')
app.config['MAIL_PASSWORD'] = 'lxcgxmvuixbkyxzg' #app password
mail=Mail(app)

from movierecsite import routes