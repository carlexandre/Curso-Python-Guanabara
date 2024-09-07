matriz = [[0,0,0],[0,0,0],[0,0,0]]
p=0
sc=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um número na posição [{l}][{c}]: '))
        if matriz[l][c]%2==0:
            p+=matriz[l][c]
        if c==2:
            sc+=matriz[l][2]
        if l==1:
            if c==0:
                maior = matriz[1][0]
            if matriz[1][c] > maior:
                maior = matriz[1][c]
    print()

print('--'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('--'*30)
print(f'A soma dos valores pares é {p}')
print(f'A soma dos valores da terceira coluna é {sc}')
print(f'O maior valor da segunda linha é {maior}\n')
