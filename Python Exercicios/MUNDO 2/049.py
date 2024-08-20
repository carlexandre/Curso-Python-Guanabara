num = int(input('Digite o número da tabuada: '))
print('A tabuada desse número é: ')
for i in range(1,11):
    t = num*i
    print(f'{num} x {i} = {t}')