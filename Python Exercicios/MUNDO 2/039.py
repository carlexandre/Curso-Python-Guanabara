anonasc = int(input('Qual o seu ano de nascimento? '))
idade = 2024 - anonasc
anoalist = anonasc+18
if idade<18:
    print(f'Você tem {idade} anos.\nAinda faltam {anoalist-idade} anos para seu alistamento.\nSeu alistamento será em {anoalist}.')
elif idade==18:
    print(f'Você tem {idade} anos.\nVocê precisa se alistar IMEDIATAMENTE.\n')
else:
    print(f'Você tem {idade} anos.\nSeu alistamento foi há {idade-18} anos.\nSeu alistamento ocorreu em {anoalist}. ')    