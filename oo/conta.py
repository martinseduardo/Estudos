class Conta:
    def __init__(self, numero, titular, saldo = 0, limite = 1000):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, deposito):
        self.__saldo += deposito
        print("Saldo: {}.".format(self.__saldo))

    def __pode_sacar(self, valor_a_sacar):
        saldo_disponivel = self.__saldo + self.__limite
        return saldo_disponivel >= valor_a_sacar

    def sacar(self, saque):
        if self.__pode_sacar(saque):
            self.__saldo -= saque
            print("Saque efetuado. Saldo: {}.".format(self.__saldo))
        else:
            print("Saldo insuficiente.")


    def extrato(self):
        print("Conta numero: {}, Titular: {}, Saldo: {} e Limite: {}.".format(self.__numero, self.__titular, self.__saldo, self.__limite))


    def transferir(self, valor, destino):
        if self.__pode_sacar(valor):
            self.sacar(valor)
            destino.depositar(valor)
            print("Transferido {} da conta {} para a conta {}. Saldo: {}".format(valor, self.__numero, destino.__numero, self.saldo))
        else:
            print("Saldo insuficiente.")

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor

    @staticmethod
    def codigo_banco():
        return "001"
