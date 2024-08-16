from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2024-08-16"
mascara_ptbr = '%d/%m/%Y %H:%M %a'
mascara_en = "%Y-%m-%d"

print(data_hora_atual.strftime(mascara_ptbr))

data_convertida = datetime.strptime(data_hora_str, mascara_en)
print(data_convertida)
