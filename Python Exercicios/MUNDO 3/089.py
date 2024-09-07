from time import sleep
boletim = list()
aluno = list()
while True:
    aluno.append(str(input('\nNome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    boletim.append(aluno[:])
    aluno.clear()
    sn = str(input('\nDeseja continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    while sn not in 'SN':
        sn = str(input('\nDeseja continuar? [S]/[N]\nSua Opção: ')).strip().upper()
    if sn=='N':
        break
print()
print(f'{'No.':<10}{'NOME':<20}{'MÉDIA'}')
print('-'*40)
for i, j in enumerate(boletim):
    print(f'{i:<10}{j[0]:<21}{((j[1]+j[2])/2):.1f}')
print('-'*40)
while True:
    pp = int(input('Deseja ver a nota de qual aluno? (999 INTERROMPE): '))
    if pp == 999:
        print('\nPROGRAMA FINALIZANDO')
        sleep(0.6)
        for i in range(0,5):
            print('.')
            sleep(0.6)
        break
    print(f'\nAs notas de {boletim[pp][0]} são {boletim[pp][1]} e {boletim[pp][2]}')
    print('-'*40)