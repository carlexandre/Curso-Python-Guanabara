from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10  ))
print(f'\nOs números escolhidos são: {numeros}')
for i in range(0,5):
    if i==0:
        maior = numeros[i]
        menor = numeros[i]
    if numeros[i]>maior:
        maior = numeros[i]
    if numeros[i]<menor:
        menor = numeros[i]
print(f'\nO maior número dentre os escolhidos é: {maior}\nO menor número dentre os escolhidos é: {menor}\n')            
