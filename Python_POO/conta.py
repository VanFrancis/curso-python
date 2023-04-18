
class Conta: 
    
    #Construtor -> inicializa o objeto
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Métodos da classe
    def extrato(self): 
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor 

    def __pode_sacar(self, valor_a_sacar): #método privado
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= (valor_disponivel_para_saque)

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor 
        else:
             print("Saldo insuficiente.. Saldo atual é {}".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property # definete o get
    def saldo(self):
        return self.__saldo

    @property 
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite): 
        self.__limite = limite