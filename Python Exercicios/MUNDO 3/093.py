jogador = dict()
listag = list()
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
print()
print(jogador)
print()
for i, j in jogador.items():
    print(f'O campo {i} tem o valor {j}')
print()
print(f'O jogador {jogador['Nome']} jogou {n} partidas.')
for i in range(1, n+1):
    print(f'{" ":<5} ⮕ Na partida {i}, fez {listag[i-1]} gols.')
print(f'Foi um total de {t} gols.')
