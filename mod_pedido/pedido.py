from flask import current_app, Blueprint, render_template, request, url_for

pedidoBP = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates/')

@pedidoBP.route('/')
def formListaPedido():
    return render_template('formPedido.html'), 200