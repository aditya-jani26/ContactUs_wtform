from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, BooleanField, SubmitField

class SignupForm(FlaskForm):
    name = StringField('name')
    email = EmailField('email')
    Message = StringField('Message')
    submit = SubmitField('submit')
    recaptcha = BooleanField('recaptcha')