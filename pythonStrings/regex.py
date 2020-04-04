import re

padrao = "[0-9]{4,5}-?[0-9]{4}"
# Vamos testar esse padrão.
texto = "Meu número para contato é 2633-5723, 98665-1960, 985398006, 26458791, 2365-1914"
retorno = re.findall(padrao, texto)
print(retorno)

for telefone in retorno:
    telefone_sem_hifem = telefone.strip()
    if len(telefone_sem_hifem) == 8:
        print(f"Telefone: {telefone}")
    else:
        print(f"Celular: {telefone}")
