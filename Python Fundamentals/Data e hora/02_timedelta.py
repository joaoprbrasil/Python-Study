from datetime import timedelta, datetime, date, time

tipo_carro = 'G'
tempo_pequeno = 30
tempo_medio = 35
tempo_grande = 50
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

print(date.today() - timedelta(days=1))

resultado = datetime(2024, 8, 16, 4, 29 ,00) - timedelta(hours=1)
print(resultado.time())

print(datetime.now().time())