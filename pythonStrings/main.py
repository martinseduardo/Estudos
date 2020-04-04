from extratorArgumentosUrl import ExtratorArgumentosUrl

url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

extrator = ExtratorArgumentosUrl(url)
extrator2 = ExtratorArgumentosUrl(url)

print(extrator.retorna_moedas())

moeda_origem, moeda_destino, valor = extrator.retorna_moedas()
print(moeda_origem, moeda_destino, valor)
#index = url.find("?")
#print(url[index + 1:])
print(extrator)
print(extrator2)
print(len(extrator))
print(extrator == extrator2)