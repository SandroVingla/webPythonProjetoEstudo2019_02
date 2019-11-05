#coding: utf-8
from flask import Blueprint, render_template, request, redirect, url_for
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm
from mod_login.login import validaSessao
from models.clienteBD import Cliente
import pymysql

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder= 'templates')

@bp_cliente.route("/", methods=['get', 'post'])
@validaSessao
def listaCliente(): 
    clientes = Cliente().selectAll()
    print(clientes)
    return render_template("listaCliente.html", clientes=clientes), 200

@bp_cliente.route('/addCliente', methods=['GET', 'POST'])
@validaSessao
def addCliente():
    cli = cliente(request.form)
    if form.validate_on_submit():
        print('valido')
    return render_template('formCliente.html', form=form), 200

@bp_cliente.route("/formCliente", methods=['POST', 'GET'])
@validaSessao
def formCliente():
    if request.form:
        cli=Cliente(request.form)
        
        


        print(request.form)

        if 'salvaEditaClienteBD' in request.form:
            print("dsdsfsfd")
           # cli.id_cliente = request.form['id_cliente']
            cli.nome  = request.form['nome']
            cli.login = request.form['login']
            cli.senha = request.form['senha']
            cli.grupo = request.form['grupo']
            cli.email = request.form['email']
            cli.endereco = request.form['endereco']
            cli.observacao = request.form['observacao']
            cli.numero = request.form['numero']
            cli.cep = request.form['cep']
            cli.bairro = request.form['bairro']
            cli.cidade = request.form['cidade']
            cli.estado = request.form['estado']
            print (cli.insert())
            
            return redirect('/')
        elif 'excluiClienteDB' in request.form:
            cli.deleteCliente()

    return render_template('/formCliente.html')
    

 


   
 