from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.frameworks.databases.memory_database import MemoryDatabase
from src_antigo.models.pedido import Pedido


class MemoryPedidoRepository(IPedidoGateway):
    def __init__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido)-> None:
        self.database.pedidos.append(pedido)

    def listar(self) -> list[Pedido]:
        return self.database.pedidos
