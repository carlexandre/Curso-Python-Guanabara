lista=[]
c = 0
while(True):
    lista.append(int(input('\nDigite um número: ')))
    sn = str(input('Você deseja continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    while sn not in 'SN':
        sn = str(input('Você deseja continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    if sn == 'N':
        break
lista.sort(reverse=True)
print(f'\nVocê digitou {len(lista)} elementos')
print(f'Os valores digitados na ordem decrescente é: {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista.')