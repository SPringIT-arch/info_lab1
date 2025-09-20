import os

def main():
    while True:
        num = input('Введите число: ')
        In = int(input("В какой СС введено данное число? "))
        Out = int(input("В какую СС нужно перевести число? "))

        print()
        print("Результат: ", ToAnotherNS(num, Out, In))
        print()

        if input("Продолжить? (Y,N): ") == "Y":
            os.system('cls')
            continue
        else:
            break



def ToAnotherNS(num, Out, In = 10):
    
    dict = {}
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    j = 10
    
    for i in alph:
        dict[j] = i
        j += 1
    
    num = int(str(num), In)
    rez = ''

    while num > 0:
        rez += str(num % Out) if num % Out < 10 else dict[num % Out]
        num //= Out
    
    return rez[::-1]


if __name__ == "__main__":
    os.system('cls')
    main()
