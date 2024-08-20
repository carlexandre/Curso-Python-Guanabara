numeros = []
print('-'*45)
mx=0
mn=0
for i in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))
maior = max(numeros)
menor = min(numeros)
for c, n in enumerate(numeros):
    if n==maior:
        mx+=1
    if n==menor:
        mn+=1    
print('-'*45)
print(f'Você digitou os valores: {numeros}\n')
if mx>1:
    print(f'O maior valor digitado foi {maior}, nas posições:', end='')
else:
    print(f'O maior valor digitado foi {maior}, na posição:', end='')
for c, n in enumerate(numeros):
    if n==maior:
        print(f' {c}', end='')
print()
if mn>1:
    print(f'O maior valor digitado foi {menor}, nas posições:', end='')
else:
    print(f'O maior valor digitado foi {menor}, na posição:', end='')
for c, n in enumerate(numeros):
    if n==menor:
        print(f' {c}', end='')
