from flask import render_template, url_for, flash, redirect
from movierecsite import app
from movierecsite.forms import SignupForm, SignInForm
from flask_bcrypt import Bcrypt
from movierecsite.models import User, Post
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

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
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #hashing password
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user) #add user to the database
        db.session.commit() #commit changes to database
        flash('Your account has been created!', 'sucess')
        return redirect(url_for('sign_in_page'))
    return render_template('sign_up.html', title='Sign Up', form=form)