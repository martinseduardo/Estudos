from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, SemDesconto


class CalculadorDeDescontos:
    def calcula(self, orcamento):
        desconto = Desconto_por_cinco_itens(Desconto_por_mais_de_quinhentos_reais(SemDesconto()))
        print(desconto.calcular(orcamento))
