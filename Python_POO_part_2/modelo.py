class Programa: 
    def _init_(self, nome, ano) -> None:
        self._nome = nome.title() 
        self.ano = ano
        self._like = 0
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def like(self):
        return self._like

    def dar_like(self):
        self._like += 1

class Filme(Programa): 
    def _init_(self, nome, ano, duracao) -> None:
        super().__init__(nome,ano)
        self.duracao = duracao
class Serie(Programa): 
    def _init_(self, nome, ano, temporada, ) -> None:
        super().__init__(nome,ano)
        self.temporada = temporada

filme = Filme("vingadores", 2018, 160)
serie = Serie("the last of us", 2023, 1)

filme.dar_like()
serie.dar_like()
serie.dar_like()
serie.dar_like()

print(f'Nome: {filme.nome} - Ano: {filme.ano} - Duração: {filme.duracao} - Likes: {filme.like}')
print(f'Nome: {serie.nome} - Ano: {serie.ano} - Duração: {serie.temporada} - Likes: {serie.like}')