from datetime import datetime



data = datetime.strptime('2026-11-18 08:50:43', '%Y-%m-%d %H:%M:%S')


print('data:  ',data.strftime('%d/%m/%Y'))
print('data e horas:',data.strftime('%d/%m/%Y %H:%M'))

print(data.year,'/',data.month,'/',data.day)
print(data.hour,':',data.minute,':',data.second)

data_actual = datetime.now()
print()
print('data actual:  ',data_actual)
print()
print(data_actual.year,'/',data_actual.month,'/',data_actual.day,' ',data_actual.hour,':',data_actual.minute,':',data_actual.second)