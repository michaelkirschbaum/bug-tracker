from flask_wtf import Form
from wtforms import StringField, PasswordField

class LoginForm(Form):
    email = StringField('email')
    password = PasswordField('password')
