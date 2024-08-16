import functools

def decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado

    return envelope

@decorador
def ola_mundo(nome, idade):
    print(f"Hello World {nome} {idade}!")
    return nome.upper()

print(ola_mundo.__name__)