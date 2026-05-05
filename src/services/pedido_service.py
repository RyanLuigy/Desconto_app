from src.models.pedido import Pedido

class PedidoService:
    """Classe de serviço para lidar com a lógica de negócios relacionada a pedidos."""

    def __init__(self, repository):
        self.repository = repository

    def adicionar_pedido(self, pedido: Pedido):
        self.repository.adicionar_pedido(pedido)

    def processar_pedidos(self):
        pedidos = self.repository.listar_pedidos()
        for pedido in pedidos:
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final a pagar: R$ {pedido.valor_final(pedido.valor_original)}")