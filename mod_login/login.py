  
from flask import current_app, Blueprint, render_template, request, url_for, redirect, session, flash
from .login_Form import LoginForm
import os

bp_login = Blueprint('/login', __name__, url_prefix='/', template_folder='templates/', static_folder='static/')

@bp_login.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        if (request.form.get('login') == 'sandro' and request.form.get('password') == 'mac123'):
            session['user'] = request.form.get('home')
            return redirect( url_for('home.home') )
        else:
            flash('senha ou usuario incorreto')
    return render_template('formLogin.html', form=form), 200

@bp_login.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    if request.method == 'POST':
        session['user'] = request.form['login']
        session.clear()
        session['user']= name 
        return redirect(url_for('login.login'))
         

