lista = []
while(True):
    lista.append(int(input('\nDigite um valor: ')))
    sn = str(input('Você deseja continuar? [S]/[N]\nSua Opção: ')).upper().strip()
    while sn not in 'SN':
        sn = str(input('Você deseja continuar? [S]/[N]\nSua Opção: ')).upper().strip()
    if sn == 'N':
        break
print(f'\nValores digitados: {lista}')
print(f'Valor(es) par(es) dessa lista: ', end='')
for i in lista:
    if i%2==0:
        print(f'{i} ', end='')
print(f'\nValor(es) impar(es) dessa lista: ', end='')        
for i in lista:
    if i%2==1:
        print(f'{i} ', end='')