sal = float(input('Digite o valor do seu salário: '))
if sal>1250:
    saln = sal*1.1
    print(f'O valor do seu novo salário será R${saln:.2f}')
else:
    saln = sal*1.15
    print(f'O valor do seu novo salário será R${saln:.2f}')    