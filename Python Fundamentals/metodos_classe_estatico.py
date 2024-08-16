class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    # cls é uma instância para a classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def maior_idade(idade):
        return idade >= 18

p = Pessoa("João", 22)
print(p.nome, p.idade)

p2 = Pessoa.criar_apartir_data_nascimento(2002, 4, 24, "Jp")
print(p2.nome, p2.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(15))