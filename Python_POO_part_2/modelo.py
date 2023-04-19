
class Filme: 
    def __init__(self, nome, ano, duracao) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__like = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def like(self):
        return self.__like

    def dar_like(self):
        self.__like += 1

class Serie: 
    def __init__(self, nome, ano, temporada, ) -> None:
        self.__nome = nome.title()
        self.ano = ano
        self.temporada = temporada
        self.__like = 0
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    @property
    def like(self):
        return self.__like
    
    def dar_like(self):
        self.__like += 1


filme = Filme("vingadores", 2018, 160)
serie = Serie("the last of us", 2023, 1)

filme.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()

print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duração: {filme.duracao} - Likes: {filme.like}')
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Duração: {serie.temporada} - Likes: {serie.like}')