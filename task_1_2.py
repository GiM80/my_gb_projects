# сумма кубов нечетных чисел
list1_cub = []
for i in range(1000):
    if i % 2 != 0:
        list1_cub.append(i ** 3)  # добавление куба числа в конец списка
print(list1_cub)

list2_cub = []
sum1 = 1
for num in list1_cub:
    i = num
    while num != 0:
        sum1 += num % 10          # суммирование чисел из остатка
        num = num // 10           # присвоение исходному операнду числа без остатка
    if sum1 % 7 == 0:             # условие целочисленного деления суммы цифр из куба числа
        list2_cub.append(i)       # добавление куба числа в конец списка
    sum1 = 0                      # обнуление списка сумм
print(sum(list2_cub))

sum_num_plus = 0
for num in list1_cub:
    summ = 0
    i = num
    num += 17
    while num != 0:
        summ += num % 10
        num = num // 10
    if summ % 7 == 0:
        sum_num_plus += i
print(sum_num_plus)