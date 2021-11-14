import random

price_list = [round(random.uniform(1, 100), 2) for i in range(20)]  # создание списка из 20 цен
print(id(price_list))  # id до сортировки
price_list.sort()  # сортировка
print(id(price_list))  # убеждаемся, что id после сортировки не изменился

revers_list = price_list.copy()[::-1]


def price(lists):
    new_list = []
    for el in lists:
        el = str(el)
        lists = el.split('.')
        stroke = f'{lists[0]} руб. {lists[1]} коп.'
        new_list.append(stroke)
    text = ', '.join(new_list)
    return text


print(price(price_list))
print(price(revers_list))
print(price(price_list[-5:]))  # вывод 5 самых дорогих товаров по возрасатнию