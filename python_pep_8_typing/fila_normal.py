from fila_base import FilaBase
from constants import CODIGO_NORMAL


class FilaNormal(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f"{CODIGO_NORMAL}{self.codigo}"
