lista= []
while(True):
    lista.append(int(input('\nDigite um valor: ')))
    if lista[-1] in lista[:-1]:
        print('Valor duplicado. Tente novamente!')
        z = lista[-1]
        lista.pop()
        lista.append(int(input('\nDigite um valor: ')))
        while lista[-1] == z:
            print('Valor duplicado. Tente novamente!')
            lista.pop()
            lista.append(int(input('\nDigite um valor: ')))
    sn = str(input('\nVocê desejar continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    while sn not in 'SN':
        sn = str(input('\nVocê desejar continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    if sn == 'N':
        break
lista.sort()
print(f'\nVocê digitou os seguintes valores: {lista}')