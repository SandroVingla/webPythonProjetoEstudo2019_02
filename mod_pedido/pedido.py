from flask import current_app, Blueprint, render_template, request, url_for, redirect, jsonify
from mod_login.login import validaSessao
from models.clienteBD import Cliente
from models.pedidoDB import Pedido
from models.pedidos_produtosBD import pedidos_produtos
from models.produtoDB import Produto

pedidoBP = Blueprint('pedido', __name__, url_prefix='/pedido', template_folder='templates/')

@pedidoBP.route('/',methods=['get', 'post'])
@validaSessao
def formListaPedido():
    pde = Pedido()
    pedidos = pde.getAll()
    return render_template('formListaPedido.html', pedidos=pedidos), 200

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
    return render_template('/formPedido.html', pagina = 'adicionar', clientes = clientes), 200

@pedidoBP.route('/editarPedido/<int:id>', methods=['get', 'post'])
@validaSessao
def formEditarPedido(id):
    pedido = Pedido()
    cliente = Cliente()
    clientes = cliente.selectAll()
    result = pedido.get(id)

    Prod = Produto()
    tdProdutos = Prod.selectALL()

    prpd = pedidos_produtos()
    produtos = prpd.getByPedidosId(id)
    

    
    return render_template('/formPedido.html', pagina = 'editar', pedido=pedido, produtos=produtos, tdProdutos = tdProdutos, clientes = clientes), 200


@pedidoBP.route('/selecionaProdutoAjax/<int:id>', methods=['get', 'post'])
@validaSessao
def selecionaProdutoAjax(id):
    Prod = Produto()
    Prod.selectProd(id)
    return jsonify({'valor':str(Prod.valor)})


@pedidoBP.route('/adicionarPedidoProduto/<int:id>', methods=['get', 'post'])
@validaSessao
def adicionarPedidoProduto(id):
   
    if 'editPedido' in request.form:
        ped = Pedido(request.form['observacoes'], request.form['id_cliente'])
        ped.id=id
        ped.update(id)


    if 'editProdutoDB' in request.form:
        print('fdsdgfdgdf')
        salvar = pedidos_produtos(
            id,
            request.form['id_produto'],
            request.form['quantidade'],
            request.form['valor'],
            request.form['observacao']
        )

         
        salvar.insert()

    return redirect(url_for('pedido.formEditarPedido', id=id))
    #return render_template('/formPedido.html', pagina = 'editar', ped = ped, cliente=cliente), 200

@pedidoBP.route('/editProduto/<int:id>', methods=['GET', 'POST'])
@validaSessao
def editProduto(id):
    print(request.form)
    prod = pedidos_produtos(request.form)
    

    if "altProduto" in request.form:
        print('formPedidl')

        prod.id_produto = request.form('id_produto')
        prod.id_pedido = request.form('id_pedido')
        prod.quantidade = request.form['quantidade']
        prod.valor = request.form['valor']
        prod.observacao = request.form['observacao']
 
        prod.update()

        return redirect(url_for('pedido.editProduto', prod=prod, id=id))


@pedidoBP.route('/delete',methods=['get','post'])
@validaSessao
def delete():

    print(request.form)
    pdr = pedidos_produtos()
    #pedido = Pedido(id)


    if 'excluiProduto' in request.form:
        print('hjdhfkjdhjdfhk')
        pdr.id_pedido=request.form['id_pedido']
        pdr.id_produto=request.form['id_produto']
            

        #pdr.pedido = request.form['id']
        #pdr.produto = request.form['id']


        pdr.delete()

        return redirect(url_for('pedido.formEditarPedido', id=request.form['id_pedido']))
    return 'erro'
    #return render_template('/delete.html', pdr=pdr, id=id, pedido=pedido,pagina = 'delete'), 200








