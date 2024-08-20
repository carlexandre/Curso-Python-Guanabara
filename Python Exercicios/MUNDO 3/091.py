from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
jogadores['Jogador 1'] = randint(1,6)
jogadores['Jogador 2'] = randint(1,6)
jogadores['Jogador 3'] = randint(1,6)
jogadores['Jogador 4'] = randint(1,6)
print('Valores Selecionados: \n')
for i, j in jogadores.items():
    print(f'{i} tirou {j}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print()
for i, j in enumerate(ranking):
    print(f'{i+1}º Lugar: {j[0]} - {j[1]}')
    sleep(1)
