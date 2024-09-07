cf = 0
ch= 0
cid = 0
erro= 0
pessoa = 1
tn = 0
dc = 1
while True:
    print(f"\nCADASTRO DE PESSOAS")
    idade = int(input(f'\nIdade: '))
    sexo = str(input('\nSexo [M]/[F]: ')).strip().upper()[0]
    while sexo not in "MF":
        sexo = str(input('\nSexo [M]/[F]: ')).strip().upper()[0]
    if idade>=18:
        cid+=1
    if sexo== 'M':  
        ch+=1
    elif sexo=='F' and idade<18:
        cf+=1
    c = str(input('\nVocê deseja continuar? [S]/[N]: ')).strip().upper()[0]
    while c not in "SN":
        c = str(input('\nVocê deseja continuar? [S]/[N]: ')).strip().upper()[0]
    if c == 'S':
        tn = 0
    elif c== 'N':
        print(f"""\nTotal de pessoas cadastradas maiores de 18 anos: {cid}\nTotal de pessoas do sexo masculino cadastradas: {ch}\nTotal de pessoas do sexo feminino menores de 18 anos cadastradas: {cf}\n\nPrograma Encerrado.""")
        break