anonasc = int(input('Ano de nascimento do atleta: '))
idade = 2024 - anonasc
if idade<=9:
    print(f'Com {idade} anos, a categoria do atleta é MIRIM.')
elif idade>9 and idade<=14:
    print(f'Com {idade} anos, a categoria do atleta é INFANTIL.')
elif idade>14 and idade<=19:
    print(f'Com {idade} anos, a categoria do atleta é JUNIOR.')
elif idade>19 and idade<=25:
    print(f'Com {idade} anos, a categoria do atleta é SÊNIOR.')
else:
    print(f'Com {idade} anos, a categoria do atleta é MASTER.')         