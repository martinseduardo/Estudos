from orcamento import Orcamento, Item
from calculador_de_impostos import CalculadorDeImpostos
from impostos import ISS, ICMS, ICPP, IKCV
from calculador_de_descontos import CalculadorDeDescontos

orcamento = Orcamento()
calculador_de_impostos = CalculadorDeImpostos()
orcamento.adiciona_item(Item("ITEM - 1", 300))
orcamento.adiciona_item(Item("ITEM - 2", 200))
orcamento.adiciona_item(Item("ITEM - 3", 100))
orcamento.adiciona_item(Item("ITEM - 4", 100))
orcamento.adiciona_item(Item("ITEM - 5", 100))
orcamento.adiciona_item(Item("ITEM - 3", 100))
calculador_de_impostos.realiza_calculo(orcamento, ICMS())
calculador_de_impostos.realiza_calculo(orcamento, ISS())
calculador_de_impostos.realiza_calculo(orcamento, ICPP())
calculador_de_impostos.realiza_calculo(orcamento, IKCV())

# orcamento = Orcamento()
# orcamento.adiciona_item(Item("ITEM - 1", 300))
# orcamento.adiciona_item(Item("ITEM - 2", 200))
# orcamento.adiciona_item(Item("ITEM - 3", 100))
# orcamento.adiciona_item(Item("ITEM - 4", 100))
# orcamento.adiciona_item(Item("ITEM - 5", 100))
# orcamento.adiciona_item(Item("ITEM - 3", 100))
# calculador_de_descontos = CalculadorDeDescontos()
# calculador_de_descontos.calcula(orcamento)
# print(orcamento.valor)
# print(orcamento.total_itens)