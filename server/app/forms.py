from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField
from wtforms import SubmitField
from wtforms.validators import Required, Length
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64)])
    password = PasswordField('Пароль', validators=[Required()])
    remember_me = BooleanField('Запомнить меня?')
    submit   = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[Required(), Length(1, 64)])
    name = StringField('ФИО', validators=[Required(), Length(1, 64)])
    password = PasswordField('Пароль', validators=[Required()])
    submit = SubmitField('Зарегистрироваться')
