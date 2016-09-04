from flask_wtf import Form
from wtforms import StringField, PasswordField

class LoginForm(Form):
    name = StringField('name')
    password = PasswordField('password')
