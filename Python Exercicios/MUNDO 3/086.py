matriz = [[],[],[]]
for i in range(0,3):
    for p in range(0,3):
        matriz[i].append(int(input(f'Digite um número na posição [{i}][{p}]: ')))
    print()
for i in range(0,3):
    for p in range(0,3):
        print(f'[{matriz[i][p]:^5}]', end='')
    print()