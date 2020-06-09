from abc import ABCMeta, abstractmethod


class Imposto(metaclass=ABCMeta):
    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto
        if self.__outro_imposto is None:
            return 0
        

    @abstractmethod
    def calcula(self, orcamento):
        pass


class TemplateDeImpostosCondicionais(metaclass=ABCMeta, Imposto):
    def calcula(self, orcamento):
        if self.deve_aplicar_imposto(orcamento):
            return self.aplica_maior_imposto(orcamento)
        else:
            return self.aplica_menor_imposto(orcamento)

    @abstractmethod
    def deve_aplicar_imposto(self, orcamento):
        pass

    @abstractmethod
    def aplica_maior_imposto(self, orcamento):
        pass

    @abstractmethod
    def aplica_menor_imposto(self, orcamento):
        pass


class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(TemplateDeImpostosCondicionais):
    def deve_aplicar_imposto(self, orcamento):
        return orcamento.valor > 500

    def aplica_maior_imposto(self, orcamento):
        return orcamento.valor * 0.07

    def aplica_menor_imposto(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(TemplateDeImpostosCondicionais):
    def deve_aplicar_imposto(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def aplica_maior_imposto(self, orcamento):
        return orcamento.valor * 0.1

    def aplica_menor_imposto(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False