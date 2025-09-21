import os

dict = {}
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
j = 10

for i in alph:
    dict[j] = i
    j += 1

def main():
    while True:
        num = input('Введите число: ')
        In = int(input("В какой СС введено данное число? "))
        Out = int(input("В какую СС нужно перевести число? "))

        print()
        print("Результат: ", result(num, Out, In))
        print()

        if input("Продолжить? (Y,N default - N): ") == "Y":
            os.system('cls')
            continue
        else:
            break


def result(num : str, Out, In = 10) -> str:
    if '.' in num: return fract(num, Out, In)
    return toanotherns(num, Out, In)


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
    num = int(num, In)
    rez = ''

    while num > 0:
        rez += str(num % Out) if num % Out < 10 else dict[num % Out]
        num //= Out
    
    return rez[::-1]


if __name__ == "__main__":
    os.system('cls')
    main()
