#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for, current_app, redirect, jsonify
from mod_login.login import validaSessao
from models.produtoDB import Produto
import pymysql
from base64 import b64encode
import os

 

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/", methods=['GET', 'POST'])
@validaSessao
def formListaProduto():
    produto = Produto()
    desc = request.args.get('descricao', '')

    if desc:
        prod = produto.selectProd(desc)
    else:
        prod=produto.selectALL()

    #imagens = []
    #for produto in prod:
       # imagens.append(b64encode(produto[3]).decode("utf-8"))

    return render_template('formListaProdutos.html', desc=desc, prod=prod),200


@bp_produto.route("/formProduto", methods=['POST'])
def formProduto():
    produto=Produto()
    return render_template('formProduto.html', produto=produto, content_type='application/json')


@bp_produto.route('/addProduto', methods=['POST'])
def addProduto():
    print(request.form)
    
    produto=Produto(request.form)
    
    produto.id_produto = request.form['id_produto']
    produto.descricao = request.form['descricao']
    produto.valor = request.form['valor']
    produto.imagem =  "data:" + request.files['imagem'].content_type + ";base64," + str(base64.b64encode( request.files['imagem'].read() ) , "utf-8")
    
    if 'addProdutoDB' in request.form:
        
        produto.insertProd()
    

    return render_template('/formProduto.html', produto=produto), 200