#coding: utf-8
from flask import Blueprint, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, IntegerField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange
from flask_wtf import FlaskForm
from mod_login.login import validaSessao
 

 

bp_cliente = Blueprint('cliente', __name__, url_prefix='/cliente', template_folder= 'templates')

@bp_cliente.route("/", methods=['get', 'post'])
@validaSessao
def formListaCliente():
    return render_template("formListaCliente.html"), 200

@bp_cliente.route("formCliente", methods=['post'])
@validaSessao
def formCliente():
    return render_template("formCliente.html"), 200

   
 