def principal():
    print("Executando a função principal")

    def funcao_interna():
        print("Executando a função interna")

    def funcao2():
        print("Executando a função2")

    funcao_interna()
    funcao2()

#funcao_interna() # ERRO
#funcao2() # ERRO
principal()