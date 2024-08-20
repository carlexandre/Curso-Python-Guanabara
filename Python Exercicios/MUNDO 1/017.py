import math 
cato = float(input('Informe o comprimento do cateto oposto: '))
cata = float(input('Informe o comprimento do cateto adjacente: '))
hip = math.sqrt((cato**2)+(cata**2))
print(f'O comprimento da hipotenusa é igual a {hip:.2f}')