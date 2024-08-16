def decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar")

    return envelope

@decorador # Açúcar sintático
def ola_mundo(nome, idade):
    print(f"Hello World {nome} {idade}!")

# ola_mundo = decorador(ola_mundo) # Sem o açúcar sintático
ola_mundo("João", 18)