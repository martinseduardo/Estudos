from projeto import ContaCorrente
from projeto import ContaPoupanca



conta1 = ContaCorrente(1)
conta2 = ContaPoupanca(2)
conta3 = ContaCorrente(3)

conta1.depositar(500)
conta2.depositar(1000)
conta3.depositar(500)
conta1.passa_mes()
conta2.passa_mes()
conta3.passa_mes()

contas = conta1, conta2, conta3
contas = sorted(contas, reverse=True)
for conta in contas:
    print(conta)

print(conta3 > conta1)

print(type(contas))
for conta in sorted(contas):
    print(conta)
