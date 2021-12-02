import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from movierecsite import app, db, bcrypt, mail
from movierecsite.forms import SignUpForm, SignInForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm
from movierecsite.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message


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
    form = SignUpForm()
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

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been successfully updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@movierecsite.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
    
If you did not make this request, then simply ignore this email and no changes will be made.
'''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('sign_in_page'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token.', 'warning')
        return redirect(url_for(reset_request))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #hashing password. Using .decode('utf-8') to make it a string instead of binary.
        user.password = hashed_password
        db.session.commit() #commit changes to database
        flash('Your password has been updated!', 'sucess')
        return redirect(url_for('sign_in_page'))
    return render_template('reset_token.html', title='Reset Password', form=form)