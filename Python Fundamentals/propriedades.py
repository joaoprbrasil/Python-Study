class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = None
        #del self._x

foo = Foo(10)
print(foo.x)
foo.x = 20
print(foo.x)

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return 2024 - self._ano_nascimento

pessoa = Pessoa("João", 2002)
print(f"Nome: {pessoa.nome} \tIdade = {pessoa.idade}")
