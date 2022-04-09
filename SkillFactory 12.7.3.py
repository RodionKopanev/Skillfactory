per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
val_percent = (per_cent.values())
money = float(input('Введите сумму вклада:'))
deposit = [i * money/100 for i in val_percent]
max_profit = str(max(deposit))
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ' + max_profit)
