num = [[],[]]
for i in range(0,7):
    n = int(input(f'Digite o {i+1}° número: '))
    if n%2==0:
        num[0].append(n)
        num[0].sort()
    else:
        num[1].append(n)
        num[1].sort()
print(f'\nOs números pares digitados foram: {num[0]}\nOs números ímpares digitados foram: {num[1]}\n')
