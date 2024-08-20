import random
from time import sleep
escolhaj = int(input('Escolha sua opção:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA\nDigite sua jogada: '))
escolhapc= random.randint(0,2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
if escolhaj<0 or escolhaj>2:
    print('JOGADA INVÁLIDA\nJOGUE NOVAMENTE\n')
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-=' *20)
print(f'O COMPUTADOR ESCOLHEU {itens[escolhapc]}.\nO JOGADOR ESCOLHEU {itens[escolhaj]}')
print('-=' *20)
if escolhapc==0:
    if escolhaj ==1:
        print('JOGADOR VENCE')
    elif escolhaj==2:
        print('COMPUTADOR VENCE')
    elif escolhaj==0:
        print('EMPATE') 
    else:
        print('JOGADA INVÁLIDA')      

elif escolhapc==1:
    if escolhaj ==1:
        print('EMPATE')
    elif escolhaj==2:
        print('JOGADOR VENCE')
    elif escolhaj==0:
        print('COMPUTADOR VENCE') 
    else:
        print('JOGADA INVÁLIDA')

elif escolhapc==2:
    if escolhaj ==1:
        print('COMPUTADOR VENCE')
    elif escolhaj==2:
        print('EMPATE')
    elif escolhaj==0:
        print('JOGADOR VENCE') 
    else:
        print('JOGADA INVÁLIDA')      