from time import sleep
opc = 4
exit = 'N'
while opc == 4 or exit=='N':
    if opc == 4:
        valrs = input('\nInforme os valores dos dois números que deseja calcular: ')
        v1, v2 = valrs.split()        
        v1 = float(v1)
        v2 = float(v2)
    if exit == 'N':
        opc = int(input('\nMENU\nEscolha uma das opções:\n\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa\n\nSua Opção: '))
        while opc!=1 and opc!=2 and opc!=3 and opc!=4 and opc!=5:
            opc = int(input('\nOPÇÃO INVÁLIDA!! TENTE NOVAMENTE.\n\nEscolha uma das opções:\n\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa\n\nSua Opção: '))
        if opc == 1:
            print(f'\nA soma de {v1} + {v2} é igual a {v1+v2:.1f}')
            exit = str(input('\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            while exit!= 'S' and exit!='N':
                exit = str(input('\nOPÇÃO INVÁLIDA!!!.\n\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            if exit == 'S':
                print('ENCERRANDO PROGRAMA')
                for i in range(0,5):
                    sleep(0.5)
                    print('.')
        elif opc == 2:
            print(f'\nA multiplicação de {v1} x {v2} é igual a {v1*v2:.1f}')
            exit = str(input('\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            while exit!= 'S' and exit!='N':
                exit = str(input('\nOPÇÃO INVÁLIDA!!!.\n\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            if exit == 'S':
                print('ENCERRANDO PROGRAMA')
                for i in range(0,5):
                    sleep(0.5)
                    print('.')
        elif opc == 3:
            if v1>v2:
                print(f'\nO número {v1} é maior que o número {v2}')
            else: 
                print(f'\nO número {v2} é maior que o número {v1}')
            exit = str(input('\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            while exit!= 'S' and exit!='N':
                exit = str(input('\nOPÇÃO INVÁLIDA!!!.\n\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            if exit == 'S':
                print('ENCERRANDO PROGRAMA')
                for i in range(0,5):
                    sleep(0.5)
                    print('.')
        elif opc == 5:
            exit = str(input('\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            while exit!= 'S' and exit!='N':
                exit = str(input('\nOPÇÃO INVÁLIDA!!!.\n\nVocê deseja sair do programa?\n\n[S]/[N]\n\nDigite sua opção: ')).upper().strip()
            if exit == 'S':
                print('ENCERRANDO PROGRAMA')
                for i in range(0,5):
                    sleep(0.5)
                    print('.')
    