from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField(label= 'Username', validators= [DataRequired(), Length(min=2, max=16)])
    email = StringField(label= 'Email', validators= [DataRequired(), Email()])
    password = PasswordField(label= 'Password', validators= [DataRequired()])
    confirm_password = PasswordField(label= 'Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField(label= 'Email', validators= [DataRequired(), Email()])
    password = PasswordField(label= 'Password', validators= [DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class UpdateAccountForm(FlaskForm):
    username = StringField(label= 'Username', validators= [DataRequired(), Length(min=2, max=16)])
    email = StringField(label= 'Email', validators= [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That email is taken. Please choose a different one.')
            
class PostForm(FlaskForm):
    title = StringField(label= 'Title', validators= [DataRequired()])
    content = TextAreaField(label= 'Content', validators= [DataRequired()])
    submit = SubmitField('Post')
    
