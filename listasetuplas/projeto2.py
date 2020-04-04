#criando listas
from collections import defaultdict

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

#usuarios = []
#usuarios.extend(usuarios_machine_learning)
#usuarios.extend(usuarios_data_science)

#usuarios = set(usuarios)

#print(usuarios)

#transformando listas em sets
usuarios_data_science = set(usuarios_data_science)
usuarios_machine_learning = set(usuarios_machine_learning)

usuarios = usuarios_machine_learning | usuarios_data_science
print(usuarios)

print(usuarios_machine_learning | usuarios_data_science) #numeros dos dois conjuntos sem repetições
print(usuarios_machine_learning & usuarios_data_science) #numeros que sao incomuns
print(usuarios_machine_learning ^ usuarios_data_science) #numeros que nao sao incomuns

usuarios.add(64)
usuarios.add(31)
print(usuarios)

usuarios = frozenset(usuarios) #conjunto imutavel
print(usuarios)
print(sorted(usuarios))
print(sorted(usuarios, reverse=True))

usuarios = {"eduardo":1, "lucy":2}
print(usuarios.get("eduardo"))

print("##################################################")

usuarios = defaultdict(int)
usuarios["lucy"] = 2
usuarios["eduardo"] = 1

for usuario in usuarios:
    print(usuario, usuarios[usuario])