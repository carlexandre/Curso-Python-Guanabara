cadastros = list()
pessoa = dict()
mulheres = list()
c=si=0
while True:
    pessoa['Nome'] = str(input('\nNome: ')).strip()
    pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    while pessoa['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()
    pessoa['Idade'] = int(input('Idade: '))
    si+=pessoa['Idade']
    cadastros.append(pessoa.copy())
    c+=1
    sn = str(input('\nQuer continuar? [S]/[N]: ')).strip().upper()
    while sn not in 'SN':
        print('\nERRO! Por favor, digite apenas S ou N.')
        sn = str(input('\nQuer continuar? [S]/[N]: ')).strip().upper()
    if sn=='N':
        break
for i in cadastros:
    if i['Sexo']=='F':
            mulheres.append(i['Nome'])
print()
print(f'-> Ao todo temos {c} pessoas cadastradas.')
print(f'-> A média de idade é de {(si/c):.2f} anos.')
print(f'-> As mulheres cadastradas foram ', end='')
for i in range(0,len(mulheres)):
    if i+1==len(mulheres):
        print(f'{mulheres[i]}')
    elif i+1==len(mulheres)-1:
        print(f'{mulheres[i]} e ', end='')
    else:
        print(f'{mulheres[i]}, ', end='')
print('-> Lista das pessoas que estão acima da média de idade: ')
for i in cadastros:
        if i['Idade']>(si/c):
            print(f'{" ":<3} Nome = {i["Nome"]} | Sexo: {i["Sexo"]} | Idade: {i["Idade"]}')
print()