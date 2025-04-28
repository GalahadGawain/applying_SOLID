from abc import ABC, abstractmethod


class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente: str = cliente
        self.itens: list = itens
        self._status: str = "Criado!"
        self.observadores: list = []

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, novo_status: str) -> None:
        self._status = novo_status
        self.notificar_observadores()

    def adicionar_observador(self, observador) -> None:
        self.observadores.append(observador)

    def notificar_observadores(self) -> None:
        for observador in self.observadores:
            observador.atualizar(self)

    @abstractmethod
    def calcular_total(self) -> None:
        pass
