from flask import current_app, Blueprint, render_template, request, url_for, redirect
from mod_login.login import validaSessao
from models.clienteBD import Cliente
from models.pedidoDB import Pedido

pedidoBP = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates/')

@pedidoBP.route('/',methods=['get', 'post'])
@validaSessao
def formListaPedido():
    return render_template('formListaPedido.html'), 200

@pedidoBP.route('/novoPedido', methods=['get', 'post'])
@validaSessao
def formPedido():
    cliente = Cliente()
    clientes = cliente.selectAll()
    if request.form:
        
        pedido = Pedido(request.form.get('observacoes'), request.form.get('id_cliente'))
        pedido.clientes_id = request.form.get('id_cliente')
        retorno = pedido.insert()
       
        if pedido.id != None:
            return redirect(url_for('pedido.formEditarPedido', id = pedido.id))
    return render_template('/formPedido.html', pagina = 'adicionar', clientes = clientes ), 200

@pedidoBP.route('/editarPedido/<int:id>', methods=['get', 'post'])
@validaSessao
def formEditarPedido(id):
    
    return render_template('/formPedido.html', pagina = 'editar'), 200