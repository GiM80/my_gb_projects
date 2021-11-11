proc = 1
while proc < 101:
    if (proc % 10 == 1) and (proc != 11):
        print(proc, "процент")
    elif ((proc % 10 == 2) or (proc % 10 == 3) or (proc % 10 == 4)) and proc // 10 != 1:
        print(proc, "процента")
    else:
        print(proc, "процентов")
    proc += 1