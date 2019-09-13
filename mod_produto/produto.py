#coding: utf-8
from flask import Blueprint, render_template, request
 


 

bp_produto = Blueprint('produto', __name__, url_prefix='/produto', template_folder='templates')

@bp_produto.route("/", methods=['get', 'post'])
def formListaProduto():
    return render_template('formListaProduto.html')

@bp_produto.route("/produto")
def formProduto():
    return render_template('formProduto.html')