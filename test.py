def toanotherns(num : str, Out : int, In = 10) -> str:
    num = int(str(num), In)
    rez = ''
    
    if str(num) == '0': return '0'

    while num > 0:
        rez += str(num % Out) if num % Out < 10 else dict[num % Out]
        num //= Out
    
    return rez[::-1]


def rever(num : str) -> str:
    if num == '0': return '0'
    if '{' not in num: return '{^'+num+'}'
    return num[num.index('^') + 1 : -1]


def tolist(num : str) -> list:
    rez = []

    while num:
        for i in range(len(num)):
            if num[i] != '{':
                rez.append(num[i])
                num = num[1:]
                break
            else:
                for j in range(len(num)):
                    if num[j] == '}':
                        rez.append(num[i:j+1])
                        num = num[j+1:]
                        break
                break

    return rez[::-1]


def tentoasym(sys : int, num : str) -> str:
    
    if str(num) == '0': return '0'

    more = int(num) > 0

    num = toanotherns(abs(num), sys)[::-1]
    rez = []
    flag = False
    
    for i in range(len(num)):
        if int(num[i], sys) + int(flag) > sys // 2:
            if int(num[i], sys) - sys + int(flag) > 0:
                rez.append(str(abs(int(num[i], sys) - sys + int(flag))))
            else:
                rez.append(rever(str(abs(int(num[i], sys) - sys + int(flag)))))
            flag = True
        else:
            if int(num[i], sys) + int(flag) > 0:
                rez.append(str(abs(int(num[i], sys) + int(flag))))
            else:
                rez.append(rever(str(abs(int(num[i], sys) + int(flag)))))
            flag = False
    
    if flag:
        rez.append(str(int(flag)))

    if more:
        return ''.join(rez[::-1])
    else:
        return ''.join(map(rever, rez[::-1]))


def asymtoten(num : list, In : int) -> int:
    rez = 0
    
    for i in range(len(num)):
        if '{' in num[i]:
            rez += -int(rever(num[i])) * (In**i)
        else:
            rez += int(num[i]) * (In**i)

    return rez





print(tentoasym(5, 1205))
print(tentoasym(5, -1205))

print(asymtoten(tentoasym(5, 1205)[1], 5))
print(asymtoten(tentoasym(5, -1205)[1], 5))

print(tolist('{^2}02{^1}0'))
print(tolist('20{^2}10'))