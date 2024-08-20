print(f'\033[1;97;40mDigite o comprimento de três retas: ')
comp = input()
a, b, c = comp.split()
a = float(a)
b = float(b)
c = float(c)
if a+b>c and b+c>a and c+a>b:
    print(f'\033[0;32;40mAs retas {a}, {b} e {c} podem formar um triângulo.')
else: 
    print(f'\033[0;31;40mAs retas {a}, {b} e {c} NÃO podem formar um triângulo.')    