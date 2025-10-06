import os
import math

fibnums = [1, 1]

for _ in range(333):
    fibnums.append(fibnums[-1] + fibnums[-2])
fibnums[0] = -1

Z = (1 + math.sqrt(5)) / 2

dict = {}
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
j = 10

for i in alph:
    dict[j] = i
    j += 1

def main():
    while True:
        num = input('Введите число: ')
        In = input("В какой СС введено данное число? ")
        Out = input("В какую СС нужно перевести число? ")

        print()
        print("Результат:", result(num, Out, In))
        print()

        if input("Продолжить? (Y,N default - N): ") == "Y":
            os.system('cls')
            continue
        else:
            break


def result(num : str, Out, In = 10) -> str:
    if Out == In: return num
    
    if '.' in num:
        if In == 'B' and Out == 'Fib':
            return tentofib(bergmantoten(num))
        if In == 'B' and Out == 'Fact':
            return tentofact(bergmantoten(num))
        if In == 'B' and int(Out) in range(1,37):
            return fract(bergmantoten(num), int(Out))

        return fract(num, int(Out), int(In))

    if In == 'Fib':
        if Out == 'Fact':
            return tentofact(str(fibtoten(num)))
        return toanotherns(fibtoten(num), int(Out))
    if Out == 'Fib':
        if In == 'Fact':
            return tentofib(str(facttoten(num)))
        return tentofib(str(int(num, int(In))))
    if In == 'Fact':
        return toanotherns(str(facttoten(num)), int(Out), In = 10)
    if Out == 'Fact':
        return tentofact(int(num, int(In)))
    return toanotherns(num, int(Out), int(In))


def tentofact(num : str) -> str:
    num = int(float(num))
    div = 2
    rez = ''

    while num != 0:
        rez += str(num % div) if num % div < 10 else dict[num % div]
        num //= div
        div += 1

    return rez[::-1]


def facttoten(num : str) -> int:
    num = num[::-1]
    for j in range(len(num)):
        if not(int(num[j], j+2)):
            return None

    rez = sum([int(num[i], 36) * math.factorial(i + 1) for i in range(len(num))])

    return rez


def fibtoten(num : str) -> int:
    if '11' in num: return None
    
    num = num[::-1]
    rez = sum([fibnums[i+1] if num[i] == '1' else 0 for i in range(len(num))])

    return rez


def tentofib(num : str) -> str:
    
    num = int(float(num))

    if num == 0: return '0'
    if num == 1: return '1'

    for ind in fibnums[::-1]:
        if num >= ind:
            if num == ind:
                return '1' + '0'*(fibnums.index(ind) - 1)
            else:
                break
    
    raz = num - ind

    return '10' + f'{tentofib(str(raz)):{0}>{fibnums.index(ind) - 2}}'


def bergmantoten(num : str) -> str:
    bd = numsep(num)[0][::-1]
    ad = numsep(num)[1]

    rezbd = sum([Z**i if bd[i] == '1' else 0 for i in range(len(bd))])
    rezad = sum([Z**(i * (-1) - 1) if ad[i] == '1' else 0 for i in range(len(ad))])

    rez = rezbd + rezad

    return str(rez)


def rmzero(strz : str) -> str:
    if '1' not in strz:
        return '0'
    for i in range(len(strz)):
        if strz[i] == '1':
            return strz[i:]


def concat(str1 : str, str2 : str) -> str:
    return str1[: -len(str2)] + str2


def fract(num : str, Out, In = 10) -> str:
    bd = beforedot(num, Out, In)
    ad = afterdot(num, Out, In)
    return bd + '.' + ad


def beforedot(num : str, Out, In = 10) -> str:
    num = totenbd(num, In)
    rez = ''

    while num > 0:
        rez += str(num % Out) if num % Out < 10 else dict[num % Out]
        num //= Out
    
    if not(rez): rez = '0'
    return rez[::-1]


def afterdot(num : str, Out, In = 10) -> str:
    num = totenad(num, In)
    rez = ''
    while num != float(0):
        num *= Out
        rez += str(int(num)) if int(num) < 10 else dict[int(num)]
        num -= int(num)
    
        if len(rez) > 100: break
    return rez


def totenbd(num : str, In) -> int:
    num = numsep(num)[0][::-1]
    rez = sum([int(num[i], In) * (In**i) for i in range(len(num))])

    return rez


def totenad(num : str, In) -> int:
    num = numsep(num)[1]
    rez = sum([int(num[i], In) * (In**(i * (-1) - 1)) for i in range(len(num))])

    return rez


def numsep(num : str) -> tuple:
    dot = num.index('.')
    bd = num[: dot]
    ad = num[dot + 1 :]

    return bd, ad


def toanotherns(num : str, Out, In = 10) -> str:
    num = int(str(num), In)
    rez = ''

    while num > 0:
        rez += str(num % Out) if num % Out < 10 else dict[num % Out]
        num //= Out
    
    return rez[::-1]


if __name__ == "__main__":
    input(
"""Справка по Системам счисления (далее - СС)

Доступны переводы из классических СС с 2 по 36

А также:

Fib - СС Фибоначчи
Fact - факториальная СС
B - СС Бергманна



                                    ───────────────────────────────────────██──────
                                    ████─████─█─█─█───████─█──█───██─████─█──█─█──█
                                    █──█─█──█─█████───█──█─█──█──█─█─█──█─█──█─█──█
                                    █──█─█─────███────█──█─████─█──█─████─█─██─████
                                    █──█─█──█─█████───█──█─█──█─█──█─█──█─██─█─█──█
                                    █──█─████─█─█─█─█─████─█──█─█──█─█──█─█──█─█──█











Выполнение работы мотивировано существованием сайта псж.онлайн                                                by SPring""")
    
    os.system('cls')
    main()
