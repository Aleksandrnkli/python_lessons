

if __name__ == '__main__':

    ##1

    # a = 4
    # b = 5
    # c = "текст"
    # d = input("Введите ваше имя: ")
    # print( f'{4} {5} {c} {d}')

    ##2

    # time_in_sec = int(input('Введите время в секундах: '))
    # hour = (time_in_sec//3600)
    # min = (time_in_sec//60)%60
    # sec = time_in_sec%60
    # if min < 10:
    #     min = '0' + str(min)
    # else:
    #     min = str(min)
    # if sec < 10:
    #     sec = '0' + str(sec)
    # else:
    #     sec = str(sec)
    # print(f'{hour}:{min}:{sec}')

    ##3

    # n = (input("Введите число n: "))
    # nn = n + n
    # nnn = nn + n
    # result = int(n) + int(nn) + int(nnn)
    # print(f"n + nn + nnn = {result}")

    ##4
    # number = input("Введите целове положительное число: ")
    # numbers = list(number)
    # numbers = sorted(numbers, reverse=True)
    #
    # print(f"Наибольшая цифра в числе {number} - {numbers[0]}")

    ##5
    # revenue = int(input("Введите выручку фирмы: "))
    # cost = int(input("Введите издержки фирмы: "))
    # if revenue > cost:
    #     print(f"Ваша прибыль составила: {revenue - cost}.")
    #     print(f"Рентабельность:{revenue/(revenue - cost)}")
    #     stuff = int(input("Введите количество сотрудников вашей фирмы: "))
    #     print(f"Прибыль в расчете на одного сотрудника: {revenue/stuff}")
    # elif cost > revenue:
    #     print("Ваша фирма работает в убыток.")
    #
    # else:
    #     print("Ваша фирма работает без прибыли и без убытка.")
    ##6
    a = int(input("Введите начальное расстояние a: "))
    b = int(input("Введите необходимое расстояние b: "))
    day = 1
    while True:
        a *= 1.1
        day+=1
        if a > b:
            break
    print(f"На {day}-й день спортсмен достиг результата - не менее {b} км.")
