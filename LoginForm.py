from wtforms import Form, StringField, PasswordField

class LoginForm(Form):
    name = StringField('name')
    password = PasswordField('password')
