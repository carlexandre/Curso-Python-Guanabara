from time import sleep
cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
cadastro['Idade'] = 2024-anonasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS']!=0: 
    cadastro['Ano de Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = int(input('Salário: R$'))
    cadastro['Aposentadoria'] = (cadastro['Ano de Contratação']+35)-2024
print()
for i, j in cadastro.items():
    if i=='Salário':
        print(f'{i}: R${j}')
    elif i=='Aposentadoria':
        print(f'Falta {j} anos para a {i}')
    elif i == 'CTPS' and j== 0:
        print(f'{i}: Não possui carteira de trabalho.')
    else:
        print(f'{i}: {j}')
    sleep(0.4)
