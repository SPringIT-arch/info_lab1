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


def tentoasym(sys : int, num : str) -> str:
    
    if str(num) == '0': return '0'

    more = int(num) > 0

    num = toanotherns(abs(num), sys)[::-1]
    rez = []
    flag = False
    
    for i in range(len(num)):
        if int(num[i], sys) > sys / 2:
            if int(num[i], sys) - sys + int(flag) > 0:
                rez.append(toanotherns(abs(int(num[i], sys) - sys + int(flag)), sys))
            else:
                rez.append(rever(toanotherns(abs(int(num[i], sys) - sys + int(flag)), sys)))
            flag = True
        else:
            if int(num[i], sys) + int(flag) > 0:
                rez.append(toanotherns(abs(int(num[i], sys) + int(flag)), sys))
            else:
                rez.append(rever(toanotherns(abs(int(num[i], sys) + int(flag)), sys)))
            flag = False
    
    if more:
        return ''.join(rez[::-1])
    else:
        return ''.join(map(rever, rez[::-1]))


# asymtoten()


print(tentoasym(3, 203575))
print(tentoasym(3, -203575))
print(toanotherns(1205, 5))
