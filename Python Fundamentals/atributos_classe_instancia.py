class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*args):
    for arg in args:
        print(arg)

estudante1 = Estudante("João", 1)
estudante2 = Estudante("Pedro", 2)
mostrar_valores(estudante1, estudante2)

Estudante.escola = "CISCO"
estudante3 = Estudante("Lorenzo", 4)
estudante1.matricula = "3"
mostrar_valores(estudante1, estudante2, estudante3)
