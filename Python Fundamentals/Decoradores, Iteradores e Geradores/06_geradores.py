def gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in gerador(numeros=[1,2,3]):
    print(i)