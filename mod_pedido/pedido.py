from flask import current_app, Blueprint, render_template, request, url_for
from mod_login.login import validaSessao

pedidoBP = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates/')

@pedidoBP.route('/',methods=['get', 'post'])
@validaSessao
def formListaPedido():
    return render_template('formListaPedido.html'), 200

@pedidoBP.route('/novoPedido', methods=['get', 'post'])
@validaSessao
def formPedido():
    return render_template('/formPedido.html'), 200