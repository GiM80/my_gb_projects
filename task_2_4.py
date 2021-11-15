price_list = [34.3, 55.34, 543.2, 100.5, 955.4, 1050.5, 20.48, 3.6, 150.45, 555.11, 999.99, 50.5, 870.35, 45.45, 6.55]

# пункт А
print("Задание по пункту 'А'")
for price_temp in price_list:
    print(f'{int(price_temp)} руб. {int(price_temp * 100 % 100):02d} коп.', end=', ')

# пункт B
print('\n\nЗадание по пункту "В"')
print(f'Список цен: {price_list} id списка цен:{id(price_list)}')
price_list.sort()
print(f'Список цен после сортировки: {price_list} id списка цен:{id(price_list)}')

# пункт C
print('\nЗадание по пункту "С"')
new_price_list = sorted(price_list.copy(), reverse=True)
print(f'Новый список цен по убыванию: {new_price_list} id нового списка цен:{id(new_price_list)}')

# пункт D
print('\nЗадание по пункту "D"')
print(price_list[-5:])