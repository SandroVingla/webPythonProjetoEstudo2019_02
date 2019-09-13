from flask import Flask, render_template, redirect, url_for, Blueprint

 
from mod_login.login import bp_login
from mod_home.home import bp_home
from mod_cliente.cliente import bp_cliente
from mod_pedido.pedido import pedidoBP  
from mod_erro.erro import bp_erro
from mod_produto.produto import bp_produto 


def create_app():
    app = Flask ( __name__ )


    app.config.from_pyfile('config.py')


    app.register_blueprint(bp_login)
    app.register_blueprint(bp_home)
    app.register_blueprint(pedidoBP)
    app.register_blueprint(bp_cliente)
    app.register_blueprint(bp_erro)
    app.register_blueprint(bp_produto)

    @app.errorhandler(404)
    def nao_encontrado(error):
        return redirect('/erro')


    return app