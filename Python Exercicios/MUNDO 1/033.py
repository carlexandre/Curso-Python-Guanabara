print('Digite o número de três números qualquer: ')
num = input()
a, b, c = num.split()
a = float(a)
b = float(b)
c = float(c)
if a>b and a>c:
    if b > c:
        print(f'O maior número é: {a}\nO menor número é: {c}')
    else:
        print(f'O maior número é: {a}\nO menor número é: {b}')
elif b>c:
    if a > c:
        print(f'O maior número é: {b}\nO menor número é: {c}')
    else:
        print(f'O maior número é: {b}\nO menor número é: {a}')
else:
    if a>b:
        print(f'O maior número é: {c}\nO menor número é: {b}')
    else:
        print(f'O maior número é: {c}\nO menor número é: {b}')