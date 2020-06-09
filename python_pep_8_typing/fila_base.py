import abc
from typing import List, Union

from constants import TAMANHO_PADRAO_MAX, TAMANHO_PADRAO_MIN
from estatistica_resumida import EstatisticaResumida
from estatistica_detalhada import EstatisticaDetalhada

Classes = Union[EstatisticaResumida, EstatisticaDetalhada]


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila: List[str] = []
    clientes_atendidos: List[str] = []
    senha_atual: str = ""

    @abc.abstractmethod
    def gera_senha_atual(self):
        ...

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAX:
            self.codigo = TAMANHO_PADRAO_MIN
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f"Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}"

    def estatisticas(self, retorna_estatistica: Classes) -> dict:

        return retorna_estatistica.roda_estatistica(self.clientes_atendidos)

