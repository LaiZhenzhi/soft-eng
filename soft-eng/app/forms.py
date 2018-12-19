from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,DateField,SelectMultipleField,SelectField,TextAreaField
from wtforms.validators import DataRequired,ValidationError,EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from app.models import Account,Data

class AccountForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(message='please input your username')])
    password = PasswordField('password',validators=[DataRequired(message='please input your password')])
    remember_me = BooleanField('remember me')
    submit = SubmitField('login')

class RegisterForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(message='please input your username')])
    password = PasswordField('password', validators=[DataRequired(message='please input your password')])
    password_check = PasswordField('check your password', validators=[DataRequired(message='please check your password'),EqualTo('password')])
    submit = SubmitField('register')

class DataForm(FlaskForm):
    content = StringField('content',validators=[DataRequired(message='add')])
    submit = SubmitField('add')
