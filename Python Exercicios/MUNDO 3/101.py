def voto(anodenascimento):
    idade = 2024-anodenascimento
    if idade>=18 and idade<=70:
        res = f'Com {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade>=16 and idade<18 or idade>70:
        res = f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        res = f'Com {idade} anos: NÃO VOTA.'
    return res


#main
anonasc = int(input('\nAno de Nascimento: '))
sit = voto(anonasc)
print()
print(sit)
