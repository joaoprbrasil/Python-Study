def mensagem(nome):
    print("Executando mensagem:")
    return f"Oi {nome}"

def mensagem_longa(nome):
    print("Executando mensagem longa:")
    return f"Olá. Tudo bem com você, {nome}?"

def executar(funcao, nome):
    print("Executando função.")
    return funcao(nome)

print(executar(mensagem, "João"))
print(executar(mensagem_longa, "João"))