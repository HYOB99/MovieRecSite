from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from movierecsite.models import User

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=2, max=20), EqualTo('password')])
    submit = SubmitField('Sign up')
    
    #check if username is already used
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() #If there's a value here, we are getting the first value. Otherwise, we get nothing.
        if user: #if user is anything other than none, it throws out an error
            raise ValidationError('Sorry, the username is taken. Please try with another one.')
    
    #check if email is already used
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() 
        if user:
            raise ValidationError('Sorry, the email is taken. Please try with another one.')
        
class SignInForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')