from abc import ABC, abstractmethod, abstractproperty
# Uma classe abstrata obriga outras classes a implementar os métodos abstratos

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando a Ar Condicionado...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a Ar Condicionado...")
        print("Desligada!")

    @property
    def marca(self):
        return "Samsung"

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)