from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor: float) -> None:
        pass
