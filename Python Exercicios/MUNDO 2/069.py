cf = 0
ch= 0
cid = 0
erro= 0
pessoa = 1
tn = 0
dc = 1
while True:
    if erro==0:
        print(f"\nCADASTRO DE PESSOAS")
        idade = int(input(f'\nIdade: '))
        sexo = str(input('\nSexo [M]/[F]: ')).strip().upper()
        dc=1
    if erro==1:
        sexo = str(input('\nSexo [M]/[F]: ')).strip().upper()
    if tn==1:
        c = str(input('\nVocê deseja continuar? [S]/[N]: ')).strip().upper()
    if idade>=18 and dc==1:
        cid+=1
    if sexo== 'M':
        erro=0
        tn=0
        if dc==1:
            ch+=1
    elif sexo=='F':
        erro=0
        tn=0
        if idade<18 and dc==1:
            cf+=1
    else:
        erro = 1
        tn = 2
        dc=0
    if tn == 0:
        c = str(input('\nVocê deseja continuar? [S]/[N]: ')).strip().upper()
        if c == 'S':
            tn = 0
        elif c== 'N':
            print(f"""\nTotal de pessoas cadastradas maiores de 18 anos: {cid}\nTotal de pessoas do sexo masculino cadastradas: {ch}\nTotal de pessoas do sexo feminino menores de 18 anos cadastradas: {cf}\n\nPrograma Encerrado.""")
            break
        else: 
            tn = 1
            erro=2
            dc=0
               
