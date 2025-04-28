from pagamento.pagamento_pix import PagamentoPIX
from pagamento.pagamento_cartao import PagamentoCartao


class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo_pagamento):
        if tipo_pagamento == "pix":
            return PagamentoPIX()
        elif tipo_pagamento == "cartao":
            return PagamentoCartao()
        else:
            raise ValueError(f"Tipo de pagamento '{tipo_pagamento}' não suportado.")
