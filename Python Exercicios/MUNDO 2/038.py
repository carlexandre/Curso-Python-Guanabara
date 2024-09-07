a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
if a>b:
    print(f'O número {a:.2f} é MAIOR que o número {b:.2f}')
elif b>a:
    print(f'O número {b:.2f} é MAIOR que o número {a:.2f}')
else:
    print(f'Os números são IGUAIS.')        