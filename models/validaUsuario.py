from flask import Blueprint, render_template , redirect , url_for , request ,session
from models.BancoDB import Banco

class ValidaUsuario(object):

    def __init__(self, id=0, username="", password="", tipo=""):
        self.info = {}
        self.id = id
        self.username = username
        self.password = password
        self.grupo = grupo

    def validaUsuario(self, username, password):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute("SELECT [id],[username] ,[password] , [grupo]  FROM [tb_usuarios].[usuarios] where username = %s and password = %s", (username , password))
            result = c.fetchall()
            c.close()
            return result 
        except:
            return None       

    def validaPermissao(self, entidade, tipo):
        
        #tipo = session['tipo']
        
        if entidade == "produto":
            if tipo != 1 and tipo != 2 : 
                return False
            else:
                return True 
        
        if entidade == "adimim":
            if tipo != 1  : 
                return False
            else:
                return True 
        return False             
