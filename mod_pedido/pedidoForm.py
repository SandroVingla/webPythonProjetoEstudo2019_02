from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import Length

class pedidoForm(FlaskForm):
    cliente = HiddenField()

    id_pedido = HiddenField()

    observacao = StringField(
        'Observação',
        validators = [
            Length(min=0, max=255, message='É permitido no máximo 255 caracteres')
        ],
        render_kw = {
            'placeholder':'Observação'
        }
    )