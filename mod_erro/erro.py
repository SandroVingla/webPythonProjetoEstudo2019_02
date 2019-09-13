#coding: utf-8
from flask import Flask, render_template, request, Blueprint


bp_erro = Blueprint('erro', __name__, url_prefix='/erro', template_folder='templates/')

@bp_erro.route('/')
def erro():
    return render_template('form404.html'), 404
    