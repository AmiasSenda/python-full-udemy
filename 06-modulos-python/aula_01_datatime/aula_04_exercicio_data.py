from datetime import datetime
from dateutil.relativedelta import relativedelta


valor_total = 1_000_000
data_emprestimo = datetime(2020, 12, 20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos


data_parcela = data_emprestimo
data_parcelas = []

while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas


print(numero_parcelas)

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), '| valor a pagar:',f'{valor_parcela:.2f} KZS')