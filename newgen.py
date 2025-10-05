import json

fibnums = [1, 1]

for _ in range(100):
    fibnums.append(fibnums[-1] + fibnums[-2])
fibnums[0] = -1

for flag in range(30,50):

    with open('labs\\infolab1\\data.json', 'r') as file:
        data = {}
        loaded = json.load(file)
        
        for kl in loaded.keys():
            zn = loaded[kl]
            if not(len(kl) == flag and kl[0] == '1'):
                data[kl] = zn

    dct = {}
    print(flag)

    templates = data.keys()
    k = 0
    for num in templates:
        if ('11' not in (f'1{num:{0}>{flag}}')) and (k == 8):
            dct[f'1{num:{0}>{flag}}'] = str(fibnums[flag + 1] + int(data[num]))
            k = 0
        else:
            k += 1

    with open('labs\\infolab1\\data.json', 'w') as file:
        json.dump({**loaded, **dct}, file)