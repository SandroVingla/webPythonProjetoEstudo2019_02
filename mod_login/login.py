  
from flask import current_app, Blueprint, render_template, request, url_for, redirect, session, flash
from .login_Form import LoginForm
from functools import wraps
from models.usuarioBD import Usuario
import os
from models.Log import Log
from models.validaUsuario import ValidaUsuario

bp_login = Blueprint('/login', __name__, url_prefix='/', template_folder='templates/', static_folder='static/')

@bp_login.route('/', methods=['GET', 'POST'])
def login(): 
    log = Log()
    log.logadorInfo("iniciando login")
    form = LoginForm(request.form)
    #login = request.form['user']
    #senha = request.form['senha']
    if form.validate_on_submit():
        login = Usuario()
        login.selectPorLogin(request.form.get('login'), request.form.get('password'))

        if  (login.id_usuario > 0):
            session.clear()
            #session['user'] = name
            
            session['user'] = request.form.get('login')           
            return redirect(url_for('home.home'))
        else:
            flash('senha ou usuario incorreto')
            
    return render_template('formLogin.html', form=form), 200
     

@bp_login.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    session.clear()  
    return redirect(url_for('/login.login'))
         
# valida se o usuário esta ativo na sessão
def validaSessao(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            #descarta os dados copiados da função original e retorna a tela de login

            return redirect(url_for('/login.login',falhaSessao=1))
        else:
            #retorna os dados copiados da função original
            return f(*args, **kwargs)

    #retorna o resultado do if acima
    return decorated_function

