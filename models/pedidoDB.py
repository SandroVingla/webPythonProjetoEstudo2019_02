from models.BancoDB import Banco 

class Pedido():

    def __init__(self, observacao='', clientes_id=None):
        self.id = None
        self.data_hora = None
        self.observacao = observacao
        self.clientes_id = clientes_id
        self.cliente_name = None


    def getAll(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT tb_pedidos.id_pedido, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente, tb_clientes.nome FROM tb_pedidos LEFT JOIN tb_clientes ON tb_pedidos.id_cliente = tb_clientes.id_cliente')
            result = c.fetchall()
            c.close()
            return result
        except:
            return None

    def getByUser(self, id):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT tb_pedidos.id, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente, tb_clientes.nome FROM tb_pedidos LEFT JOIN tb_clientes ON tb_pedidos.id_cliente = tb_clientes.id WHERE tb_pedidos.id_cliente = %s', (id))
            result = c.fetchall()
            c.close()
            return result
        except:
            return None


    def get(self, id_pedido):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('SELECT tb_pedidos.id_pedido, tb_pedidos.data_hora, tb_pedidos.observacao, tb_pedidos.id_cliente FROM tb_pedidos   WHERE tb_pedidos.id_pedido = %s' , (id_pedido))
            for linha in c:
                self.id=linha[0]
                self.data_hora=linha[1]
                self.observacao=linha[2]
                self.clientes_id=linha[3]
                
            c.close()
            if not self.id:
                return 'Pedido não encontrado!'
            return 'Busca feita com sucesso!'
        except:
            return 'Ocorreu um erro na busca do pedido'


    def insert(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute('INSERT INTO tb_pedidos(observacao, id_cliente) VALUES(%s, %s)' , (self.observacao, self.clientes_id))
            banco.conexao.commit()
            self.id = c.lastrowid
            c.close()
            return 'Pedido cadastrado com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do pedido'


    def update(self):
        banco=Banco()
        #try:
        c=banco.conexao.cursor()
        c.execute('UPDATE tb_pedidos SET observacao = %s , id_cliente = %s WHERE id_pedido = %s' , ( self.observacao , self.clientes_id, self.id))
        banco.conexao.commit()
        c.close()
        return 'Pedido atualizado com sucesso!'
       # except:
            #return 'Ocorreu um erro na alteração do pedido'


    def delete(self):
        banco=Banco()
        try:
            c=banco.conexao.cursor()
            c.execute('DELETE FROM tb_pedidos WHERE id = %s' , (self.id))
            banco.conexao.commit()
            c.close()
            return 'Pedido excluído com sucesso!'
        except:
            return 'Ocorreu um erro na exclusão do pedido'