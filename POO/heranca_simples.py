# Herança simples
class Veiculo:
    def __init__(self, cor, placa, numeros_rodas):
        self.cor = cor
        self.placa = placa
        self.numeros_rodas = numeros_rodas

    def ligar_motor(self):
        print("Ligando o motor...")

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def carregado(self):
       print(f"{'Sim' if self.carregado else 'Não'}")




caminhao = Caminhao("preto", 123, 12, True)
caminhao.ligar_motor()
Caminhao.carregado(caminhao)