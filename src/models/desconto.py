from abc import ABC, abstractmethod

class IDesconto(ABC):
    @abstractmethod
    def calcular_desconto(self, valor: float) -> float:
        raise NotImplementedError

class DescontoNormal (IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.1
    
class DescontoVIP (IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.2
    
class DescontoPremium (IDesconto):
    def calcular_desconto(self, valor: float) -> float:
        return valor * 0.3