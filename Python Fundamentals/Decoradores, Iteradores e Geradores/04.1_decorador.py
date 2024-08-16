def decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")

    return envelope

@decorador # Açúcar sintático
def ola_mundo():
    print("Ola mundo")

# ola_mundo = decorador(ola_mundo) # Sem o açúcar sintático
ola_mundo()