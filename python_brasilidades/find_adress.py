import requests

class AdressFinder:
    def __init__(self, cep):
        self.cep = str(cep)
        self.rua = None
        self.bairro = None
        self.cidade = None
        self.uf = None
        if len(self.cep) == 8:
            self.adress_finder(self.cep)
        else:
            raise ValueError("Quantidade de digitos inválida!")

    def __str__(self):
        return f"Endereço: Rua {self.rua}, {self.bairro}\n" \
               f"{self.cidade}, {self.uf} - CEP {self.cep}"

    def adress_finder(self, number):
        url = requests.get("https://viacep.com.br/ws/{}/json".format(number))
        adress = url.json()
        self.cep = adress.get("cep")
        self.rua = adress.get("logradouro")
        self.bairro = adress.get("bairro")
        self.cidade = adress.get("localidade")
        self.uf = adress.get("uf")
        self.ibge = adress.get("ibge")


