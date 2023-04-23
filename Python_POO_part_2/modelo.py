class Programa: 
    def __init__(self, nome, ano):
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
        
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Likes: {self.like}'
class Filme(Programa): 
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self.nome} - Duração: {self.duracao} min - Ano: {self.ano} - Likes: {self.like}'
class Serie(Programa): 
    def __init__(self, nome, ano, temporada, ):
        super().__init__(nome,ano)
        self.temporada = temporada
    
    def __str__(self):
        return f'Nome: {self.nome} - Temporadas: {self.temporada} - Ano: {self.ano} - Likes: {self.like}'

class Plalist():
    def __init__(self, nome, programa):
        self.nome = nome 
        self._programa = programa
    
    @property
    def listagem(self):
        return self._programa
    
    @property
    def __len__(self):
        return len(self._programa)
    
    def __getitem__(self, item):
        return self._programa[item]
    

filme = Filme("vingadores", 2018, 160)
filme2 = Filme("Super Mario", 2023, 120)
serie = Serie("the last of us", 2023, 1)
serie2 = Serie("the bear", 2022, 1)

filme.dar_like()
filme2.dar_like()
filme2.dar_like()
filme2.dar_like()
serie.dar_like()
serie.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()
serie2.dar_like()

filmes_e_series = [filme, serie, filme2, serie2]

for programa in filmes_e_series:
    print(programa)