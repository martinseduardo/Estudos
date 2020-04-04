class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.string_eh_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url Invalida.")

    def __str__(self):
        moeda_origem, moeda_destino, valor = self.retorna_moedas()
        return f"Conteudo extraido: Moeda origem: {moeda_origem}, Moeda destino: {moeda_destino} e Valor: {valor}."

    def __len__(self):
        return len(self.url)

    def __eq__(self, outro_objeto):
        return self.url == outro_objeto.url

    @staticmethod
    def string_eh_valida(url):
        if url and url.startswith("https://www.bytebank.com.br/cambio"):
            return True
        else:
            return False

    def retorna_moedas(self):
        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="

        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

        if moeda_origem == "moedadestino":
            moeda_origem = self.verifica_moeda_origem(busca_moeda_origem)

        inicio_substring_moeda_destino = self.encontra_indice_inicio_substring(busca_moeda_destino)
        final_substring_moeda_destino = self.url.find("&valor")
        moeda_destino = self.url[inicio_substring_moeda_destino:final_substring_moeda_destino]

        return moeda_origem, moeda_destino, self.retorna_valor()

    def encontra_indice_inicio_substring(self, moeda_ou_valor):
        return self.url.find(moeda_ou_valor) + len(moeda_ou_valor)

    def verifica_moeda_origem(self, busca_moeda_origem):
        self.url = self.url.replace("moedadestino", "real", 1)  # primeiro vou fazer sem o 1 e depois vou usa-lo
        inicio_substring_moeda_origem = self.encontra_indice_inicio_substring(busca_moeda_origem)
        final_substring_moeda_origem = self.url.find("&")
        return self.url[inicio_substring_moeda_origem:final_substring_moeda_origem]

    def retorna_valor(self):
        busca_valor = "Valor=".lower()
        inicio_substring_valor = self.encontra_indice_inicio_substring(busca_valor)
        valor = self.url[inicio_substring_valor:]
        return valor
