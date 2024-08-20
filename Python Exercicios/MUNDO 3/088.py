from random import randint
from time import sleep
print(f'\n{'MEGA SENA':^43}\n')
qnts = int(input('Quantidade de jogos: '))
jogos = list()
jogo = list()
print(f'\n{f'SORTEANDO {qnts} JOGOS':^43}\n')
for i in range(0,qnts):
    for i in range(0,6):
        num = randint(1,60)
        while num in jogo:
            num = randint(1,60)
        jogo.append(num)
        jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for i in range(0,qnts):
    sleep(0.5)
    print(f'{i+1}º Jogo: {jogos[i]}')
print()