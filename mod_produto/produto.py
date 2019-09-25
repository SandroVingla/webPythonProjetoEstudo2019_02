#coding: utf-8
from flask import Blueprint, render_template, request
from mod_login.login import validaSessao


 

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/", methods=['get', 'post'])
@validaSessao
def formListaProduto():
    return render_template('formListaProduto.html')

@bp_produto.route("/produto")
@validaSessao
def formProduto():
    return render_template('formProduto.html')