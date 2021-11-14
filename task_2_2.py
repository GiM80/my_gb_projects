main_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(main_list):
    if s.isdigit():
        main_list[i] = f'"{int(s):2d}"'
    elif s[1:].isdigit():
        main_list[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(s, end=' ')
