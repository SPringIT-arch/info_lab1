fibnums = [1, 1]

for _ in range(200):
    fibnums.append(fibnums[-1] + fibnums[-2])
fibnums[0] = -1


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

