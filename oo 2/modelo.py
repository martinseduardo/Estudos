class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    def __str__(self):
        return (f"Filme: {self._nome} / Likes: {self._likes}")

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return (f"Filme: {self.nome} / {self.duracao} Min / Likes: {self.likes}")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return (f"Serie: {self.nome} / {self.temporadas} Temporada(s) / Likes: {self.likes}")

class Playlist:
    def __init__(self, nome, programas):
        self._nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


vingadores = Filme("avengers - endgame", 2019, 180)
the_boys = Serie("the boys", 2017, 1)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
the_boys.dar_like()
the_boys.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

listinha = [the_boys, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist)}')


# print(f"Filme: {vingadores.nome} / Likes: {vingadores.likes}")
# print(f"Serie: {the_boys.nome} / Likes: {the_boys.likes}")