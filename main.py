from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus


cliente = Cliente("Laís", "Alura")
item_um = Item("Pizza", 30.0)
item_dois = Item("Refrigerante", 5.0)
itens = [item_um, item_dois]

taxa_entrega = 10.0
pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = "Pagamento processado com sucesso!"
MENSAGEM_PREPARANDO = "Seu pedido está sendo preparado!"
MENSAGEM_ENVIADO = "Seu pedido foi enviado!"
MENSAGEM_ENTREGUE = "Seu pedido foi entregue!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observador(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
pedido.status = MENSAGEM_ENTREGUE

if __name__ == "__main__":
    pass
