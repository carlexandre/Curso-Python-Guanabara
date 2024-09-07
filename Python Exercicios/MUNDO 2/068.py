from random import randint
cont = 0
erro = 0
print('JOGO | PAR OU ÍMPAR')
while True:
    if erro == 1:
        choic = str(input('\nVocê quer PAR[P] ou ÍMPAR[I]\nSua Opção: ')).strip().upper()
    if erro == 0:
        njg = int(input('\nDigite um valor: '))
        choic = str(input('\nVocê quer PAR[P] ou ÍMPAR[I]\nSua Opção: ')).strip().upper()
    npc = randint(1,100000)    
    val = npc+njg
    if choic == 'P':
        erro=0
        if val%2==0:
            cont+=1
            print(f'\nPAR!!! Você GANHOU!!!\n\nNúmero PC: {npc}\nNúmero Jogador: {njg}\nTotal: {val}\n\nVitórias seguidas: {cont}')
        else:
            print(f"\nÍMPAR!!! Você Perdeu.\n\nNúmeroPC: {npc}\nNúmero Jogador: {njg}\nTotal: {val}\n\nVitórias acumuladas: {cont}\n")
            break 
    elif choic == 'I':
        erro=0
        if val%2==1:
            cont+=1
            print(f'\nÍMPAR!!! Você GANHOU!!!\n\nNúmero PC: {npc}\nNúmero Jogador: {njg}\nTotal: {val}\n\nVitórias seguidas: {cont}')
        else:
            print(f"PAR!!! Você Perdeu.\n\nNúmero PC: {npc}\nNúmero Jogador: {njg}\nTotal: {val}\n\nVitórias acumuladas: {cont}\n")
            break
    else:
        print('Opção Inválida!! Tente novamente.')
        erro=1    


        
