from datetime import datetime
from movierecsite import db
#creating user model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #it is going to be a primary key and it's unique.
    username = db.Column(db.String(20), unique=True, nullable=False) #Max 20 characters. It can't be a null value.
    email = db.Column(db.String(120), unique=True, nullable=False) #Max 120 characters. Can't be a null value. 
    password = db.Column(db.String(60), nullable=False) #Also hasing password, so 60 max characters for password.
    posts = db.relationship('Post', backref='author', lazy=True) #has a relationship to post model. Backref is a simply way to declare a new property of on the Post class. Lazy defines when SQLAlchemy will load the data from the databse.
    
    def __repr__(self): #How our object is printed
        return f"User('{self.username}', '{self.email}')"

#creating post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True) #it is going to be a primary key and it's unique.
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) #id of an author. 
    def __repr__(self): #How our object is printed
        return f"Post('{self.title}','{self.date_posted}')"