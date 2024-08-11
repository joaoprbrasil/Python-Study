#   Classe:
#   Uma classe define as características e comportamentos de um objeto, porém não conseguimos
#   usá-las diretamente.
class Bicicleta:
    # self representa a instância do objeto
    # método construtor __init__
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


#   Métodos:
    def buzinar(self):
        print("Plim plim!")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmmmmmm...")

    #def __str__(self):
    #    return f"Bicicleta = cor : {self.cor}, modelo : {self.modelo}, ano: {self.ano}, valor : {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo instância da classe.")

    def falar(self):
        print("Falando...")

#   Objetos:
#   Os objetos são instâncias de uma classe que podemos usá-los. Eles possuem características
#   e comportamentos que foram definidos nas calsses.

bike1 = Bicicleta("vermelha", "caloi", 2022, 1200)
bike1.buzinar()
bike1.parar()
bike1.correr()
print(bike1.cor)
Bicicleta.buzinar(bike1)
print(bike1)



cachorro = Cachorro("dog", "preto")
cachorro.falar()
