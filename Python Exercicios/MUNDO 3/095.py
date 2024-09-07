jogadores=list()
jogador = dict()
listag = list()
while True:
    t=0
    jogador['Nome'] = str(input('\nNome do Jogador: '))
    n = int(input(f'Quantidade de partidas que {jogador['Nome']} jogou: '))
    print()
    for i in range(1, n+1):
        g = int(input(f'Quantidade de gols na partida {i}: '))
        t+=g
        listag.append(g)
    jogador['Gols'] = listag[:]
    jogador['Total de Gols'] = t
    jogadores.append(jogador.copy())
    listag.clear()
    sn = str(input('\nDeseja continuar? [S]/[N]: ')).upper().strip()
    while sn not in 'SN':
        print('\nERRO! Digite apenas S ou N.')
        sn = str(input('Deseja continuar? [S]/[N]: ')).upper().strip()
    if sn=='N':
        break
print()
print(f'{f'Cód'} {f'Nome':<15} {'Gols':<13} {f'Total':<13}')
print('-'*46)
for i, j in enumerate(jogadores):
    print(f'{i:>2}', end=' ')
    for v in j.values():
        print(f'{str(v):<16}', end='')
    print()
print('-'*46)
while True:
    md = int(input('\nMostrar dados de qual jogador? (999 para parar)'))
    while md<0 or md>len(jogadores)-1:
        print('\nERRO! Digite um código existente.')
        md = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if md==999:
        break
    print(f'-> Levantamento do jogador {jogadores[md]['Nome']}:\n')
    for i in range(1, len(jogadores[md]['Gols'])+1):
        print(f'{" ":<5} Na partida {i}, fez {jogadores[md]['Gols'][i-1]} gols.')
