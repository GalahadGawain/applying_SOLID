class ObservadorStatus:
    def __init__(self, notificacoes):
        self.notificacoes: str = notificacoes

    def atualizar(self, pedido):
        mensagem: str = f"Atualização: {pedido.status}"
        self.notificacoes.enviar_notificacoes(pedido.cliente, mensagem)
