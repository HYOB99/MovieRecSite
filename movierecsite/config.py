import os

class Config:
    SECRET_KEY = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #specifying the relative path to the current file
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_ADD_PROJ')
    MAIL_PASSWORD = 'lxcgxmvuixbkyxzg' #app password