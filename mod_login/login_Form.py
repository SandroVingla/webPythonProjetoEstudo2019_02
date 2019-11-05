from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    login = StringField(
        'Login',
        validators = [
            DataRequired(message="Campo obrigatório")
        ],
        render_kw = {
            'placeholder':'Login'
        }
    )

    password = PasswordField(
        'password',
        validators = [DataRequired(message="Campo obrigatório")],
        render_kw = {
            'placeholder':'Senha'
        }
    )

    remember_me = BooleanField("salvar senha")
     

    