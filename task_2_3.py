first_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАй',
              'директор аэлита']

for el in first_list:
    first_name = el.split(' ')[-1].title()
    print(f'Привет, {first_name}!')