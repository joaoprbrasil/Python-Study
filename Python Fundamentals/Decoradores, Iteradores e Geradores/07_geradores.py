def gerador():
    yield 1

for i in gerador():
    print(i)