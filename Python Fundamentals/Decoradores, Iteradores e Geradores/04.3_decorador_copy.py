def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado

    return envelope

@decorador
def ola_mundo(nome, idade):
    print(f"Hello World {nome} {idade}!")
    return nome.upper()

resultado = ola_mundo("João", 18)
print(resultado)
print(ola_mundo.__name__)