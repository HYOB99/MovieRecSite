from flask import render_template, url_for, flash, redirect, request
from movierecsite import app, db, bcrypt
from movierecsite.forms import SignupForm, SignInForm
from movierecsite.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


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
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next') #This is to simply redirect to a page that a user was trying to access before logging in.
            return redirect(next_page) if next_page else redirect(url_for('main_page')) #redirects to the next page if it exists. Otherwise, go to home page.
        else:
            flash('Login Failed. Please check email and paassword', 'danger')
    return render_template('sign_in.html', title='Sign In', form=form)

@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up_page():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #hashing password. Using .decode('utf-8') to make it a string instead of binary.
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user) #add user to the database
        db.session.commit() #commit changes to database
        flash('Your account has been created!', 'sucess')
        return redirect(url_for('sign_in_page'))
    return render_template('sign_up.html', title='Sign Up', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main_page'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')