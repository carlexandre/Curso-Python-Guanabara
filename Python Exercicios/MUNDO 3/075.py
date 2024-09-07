a = int(input('\nDigite um valor: '))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
d = int(input('Digite um valor: '))
num = (a, b, c, d)
pares = ''
print(f'\nO valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'\nO valor 3 está na {num.index(3)+1}º posição.')
else:
    print(f'\nO valor 3 não está em nenhuma posição')
print(f'\nOs valores pares digitados foram: ', end='')
for i in num:
    if i%2==0:
        print(f'{i} ', end='')    