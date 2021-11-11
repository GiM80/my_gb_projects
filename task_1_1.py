input_sec = int(input("Введите количество секунд: "))
sec = input_sec % (24 * 60 ** 2)
hour = sec // (60 ** 2)
sec = sec % (60 ** 2)
minute = sec // 60
sec = sec % 60
print(hour, "час.", minute, "мин.", sec, "сек.")