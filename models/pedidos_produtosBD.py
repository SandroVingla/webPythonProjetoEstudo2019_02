from models.BancoDB import Banco

class pedidos_produtos():

    def __init__(self, id_pedido=0, id_produto=None, quantidade=None, valor=None, observacao=''):
        self.id = None
        self.id_pedido = id_pedido
        self.id_produto= id_produto
        self.quantidade = quantidade
        self.valor = valor
        self.observacao = observacao


    def getByPedidosId(self, id_pedido):
        banco=Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT tb_pedidos_produtos.id_pedido, tb_pedidos_produtos.id_produto, tb_pedidos_produtos.quantidade, tb_pedidos_produtos.valor, tb_pedidos_produtos.observacao, tb_produtos.descricao, tb_produtos.valor, CONVERT(tb_produtos.imagem USING utf8) FROM tb_pedidos_produtos LEFT JOIN tb_produtos ON tb_pedidos_produtos.id_produto = tb_produtos.id_produto WHERE tb_pedidos_produtos.id_pedido = %s' , (id_pedido))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    
    def getBypedidos_produtos(self, id_pedido, id_produto):
        banco=Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('SELECT id_pedido, id_produto, quantidade, valor, observacao FROM pedidos_produtos WHERE id_pedido = %s AND id_produto = %s' , (id_pedido, id_produto))
            for linha in c:
                self.id_pedido=linha[0]
                self.id_produto=linha[1]
                self.quantidade=linha[2]
                self.valor=linha[3]
                self.observacao=linha[4]
                return True
            c.close()
            return False
        except:
            return False


    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO tb_pedidos_produtos(id_pedido, id_produto, quantidade, valor, observacao) VALUES (%s, %s, %s, %s, %s)' , (self.id_pedido, self.id_produto, self.quantidade, self.valor, self.observacao))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Produto do pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto do pedido'


    def update(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('UPDATE tb_pedidos_produtos SET  quantidade = %s, valor = %s, observacao = %s WHERE id_pedido = %s AND id_produto = %s' , (self.quantidade, self.valor, self.observacao, self.id_pedido, self.id_produto))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido atualizado com sucesso!'
        except:
            return 'Ocorreu um erro na alteração do produto do pedido'


    def delete(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM tb_pedidos_produtos WHERE id_pedido = %s AND id_produto = %s' , (self.id_pedido, self.id_produto))
            banco.conexao.commit()
            c.close()
            return 'Produto do pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do produto do pedido'

    
    def deleteByPedido(self, id_pedido):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM tb_pedidos_produtos WHERE id_pedido = %s' , (id_pedido))
            banco.conexao.commit()
            c.close()
            return True
        except:
            return False


    def hasByProduct(self, id_produto):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT COUNT(id_pedido) FROM tb_pedidos_produtos WHERE tb_pedidos_produtos.produtos_id = %s', (id_produto))
            result = c.fetchall()
            c.close()
            if result[0][0] > 0:
                return True
            return False
        except:
            return False