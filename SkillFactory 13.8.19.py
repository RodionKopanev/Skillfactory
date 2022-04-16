tickets = int(input('Введите количество билетов: '))
result = 0
for i in range(1, tickets+1):
    age = int(input(f'Введите возраст {i}-ого покупателя: '))
    if age < 18:
        print('Стоимость билета 0 рублей')
    elif 18 <= age < 25:
        print('Стоимость билета 990 рублей')
        result += 990
    elif age >= 25:
        print('Стоимость билета 1390 рублей')
        result += 1390
if tickets > 3:
    result *= 0.9
print(f'Общая стоимость билетов = {result} рублей')
