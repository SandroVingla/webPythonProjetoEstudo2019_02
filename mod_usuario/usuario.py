import os
from flask import current_app, Blueprint, render_template, request, url_for, redirect
from .usuarioForm import usuarioForm
from mod_login.login import validaSessao
from models.usuarioBD import Usuario
import pymysql

bp_usuario = Blueprint('usuario', __name__, url_prefix='/usuario', template_folder='templates', static_folder='static')

@bp_usuario.route('/')
@validaSessao
def index():
    return render_template('usuario.html'), 200

@bp_usuario.route('/add', methods=['GET', 'POST'])
@validaSessao
def add():
    form = usuarioForm(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('usuarioAdd.html', form=form), 200

@bp_usuario.route('/addUser', methods=['POST'])
def addUser():
    
    user= Usuario()
    
    user.id_usuario = request.form['id_usuario']
    user.nome  = request.form['nome']
    user.login = request.form['login']
    user.senha = request.form['senha']
    user.grupo = request.form['grupo']

    executou = user.insertUser()
    print(executou)
    print("cadastrado com sucesso")
    
    return redirect('/')
     