from collections import defaultdict
from collections import Counter

texto1 = """O Ministério da Saúde divulgou o mais recente balanço dos casos da Covid-19, doença causada pelo coronavírus Sars-Cov-2. Os principais números são:

92 mortes
3.417 casos confirmados
2,7% é a taxa de letalidade
São Paulo concentra 1.223 casos, e o Rio, 493.
No balanço anterior, que marcou o primeiro mês da circulação do novo coronavírus Sars-Cov-2 no Brasil, os números apontavam 77 mortes e 2.915 casos confirmados. Em relação às mortes, o aumento foi de 19%, e de 17% em relação aos casos do dia anterior.

VÍDEOS: incubação, sintomas e mais perguntas e respostas
BOATOS: O que é #FATO ou #FAKE sobre o coronavírus
GRUPOS VULNERÁVEIS: veja quais grupos têm mais complicações
SINTOMAS: febre, tosse e dificuldade de respirar, entenda em detalhes
Perfil dos mortos
O secretário de vigilância do Ministério da Saúde, Wanderson Kleber de Oliveira, disse que o perfil das vítimas mostra que, entre as pessoas com entre 20 e 39 anos, foram registradas três mortes. Entre 40 e 59 anos, o total de mortes chega a seis. Já outras 76 mortes ocorreram no grupo de pacientes com mais de 60 anos."""

texto2 = """As autoridades italianas afirmaram que o número diário de mortes na quinta-feira foi de 919; o total chegou a 9.134.
Por G1

27/03/2020 13h41  Atualizado há 12 minutos

Na Itália, caixões são levados ao interior de uma igreja — Foto: Claudio Furlan/LaPresse via APNa Itália, caixões são levados ao interior de uma igreja — Foto: Claudio Furlan/LaPresse via AP
Na Itália, caixões são levados ao interior de uma igreja — Foto: Claudio Furlan/LaPresse via AP

O número de mortes na Itália por causa do Covid-19, a doença causada pelo coronavírus aumentou em 919, disse a agência de proteção civil nesta sexta-feira (27). Até agora, 9.143 pessoas morreram por conta da epidemia no país.

É o recorde para um único dia. Antes, havia sido o 21 de março, quando 793 pessoas haviam morrido. No entanto, 50 delas são referentes à mortes de quinta-feira, na região do Piemonte, que foram contabilizadas nesta sexta-feira.

Nos últimos dias, os números foram os seguintes:

23 de março: 602
24 de março: 743
25 de março: 683
26 de março: 712
27 de março: 919
Na Itália, muita gente ainda segue desrespeitando a quarentena

Prefeito de Milão
A região mais atingida é a da Lombardia, onde fica a cidade de Milão. Lá, houve 5.402 mortes.

No dia 22 de março, durante uma entrevista à TV RAI, o prefeito de Milão, Giuseppe Sala, afirmou que errou ao divulgar, no fim de fevereiro, um vídeo que dizia que a cidade não pode parar.

“Muitos se referem àquele vídeo que circulava com o título ’Milão não Para’. Era 27 de fevereiro, o vídeo estava explodindo nas redes, e todos o divulgaram, inclusive eu. Certo ou errado? Provavelmente, errado”, ele afirmou à RAI no domingo (22).

Ainda não chegou o pico
As infecções de coronavírus na Itália não atingiram seu pico, disse Silvio Brusaferro, chefe do Instituto Superior de Saúde do país nesta sexta-feira (27).

PANDEMIA: veja quais países já registraram casos da doença
GUIA ILUSTRADO: sintomas, transmissão e prevenção
CORONAVÍRUS: veja perguntas e respostas
“Não atingimos o pico e não passamos dele”, disse Brussaferro.

Ele disso que há, no entanto, sinais de uma desaceleração no número de pessoas que estão ficando infectadas, o que sugere que o pico não está longe. Depois disso, os novos casos vão entrar em tendência visível de queda.

“O nosso comportamento vai influenciar em quão íngreme vai ser a queda, quando ela começar”, afirmou ele, em uma referência à aderência dos italianos às restrições ao movimento impostas pelo governo.

Mortes na Espanha
A Espanha é o segundo país da Europa mais atingido pela pandemia. Lá, foram 769 mortes nas últimas 24 horas. Ao todo, são 4.858 mortes."""



def frenquencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())
    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}%.".format(caractere, proporcao * 100))


frenquencia_de_letras(texto1)
#frenquencia_de_letras(texto2)