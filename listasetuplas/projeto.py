from functools import total_ordering

@total_ordering
class ContaBancaria:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def __eq__(self, other):
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __lt__(self, other):
        return self._codigo < other._codigo

    def __str__(self):
        return f"### COdigo: {self._codigo} / Saldo: {self._saldo} ###"

class ContaCorrente(ContaBancaria):
    def passa_mes(self):
        self._saldo -= 2

    def __str__(self):
        return f"### Conta Corrente / COdigo: {self._codigo} / Saldo: {self._saldo} ###"


class ContaPoupanca(ContaBancaria):
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 2

    def __str__(self):
        return f"### Conta Poupança / COdigo: {self._codigo} / Saldo: {self._saldo} ###"
