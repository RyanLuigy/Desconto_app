from src.services.pedido_service import PedidoService
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedido import Pedido

if __name__ == "__main__":
    service = PedidoService()

    """Criando pedidos e descontos"""

