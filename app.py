from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import SignupForm, SignInForm
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c4ebd5c19784795cce458b28cf63e20a' #Used Secrets module in python to generate a secret key to protect against some potential attacks. 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #specifying the relative path to the current file
db = SQLAlchemy(app)

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

@app.route("/")
@app.route("/home")
def main_page():
    return render_template('home.html')

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route("/recent_movies")
def recent_movies_page():
    return render_template('recent_movies.html', title='Recent Movies')

@app.route("/genres")
def genres_page():
    return render_template('genres.html', title='Genres')

@app.route("/sign_in", methods=['GET', 'POST'])
def sign_in_page():
    form = SignInForm()
    return render_template('sign_in.html', title='Sign In', form=form)

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up_page():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'sucess')
        return redirect(url_for('main_page'))
    return render_template('sign_up.html', title='Sign Up', form=form)