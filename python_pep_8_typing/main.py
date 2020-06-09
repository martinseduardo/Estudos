from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

teste = FabricaFila.pega_fila("prioritaria")
teste.atualiza_fila()
teste.atualiza_fila()
teste.atualiza_fila()
teste.atualiza_fila()
print(teste.chama_cliente(10))
print(teste.chama_cliente(10))
print(teste.chama_cliente(10))
print(teste.chama_cliente(10))
print(teste.estatisticas(EstatisticaDetalhada("01/01/2020", 120)))
