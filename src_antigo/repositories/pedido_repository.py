from src_antigo.database.connection import DatabaseConnection
from src_antigo.models.pedido import Pedido

class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar os pedidos."""

    def __init__(self, database: DatabaseConnection):
        self.database = database

    def adicionar_pedido(self, pedido: Pedido):
        self.database.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.database.pedidos