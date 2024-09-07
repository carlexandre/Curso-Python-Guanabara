n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
if media>=7:
    print(f'A média do aluno é: {media:.1f}\nAPROVADO')
elif media<5:
    print(f'A média do aluno é: {media:.1f}\nREPROVADO')
elif media>=5 and media<7:
    print(f'A média do aluno é: {media:.1f}\nRECUPERAÇÃO')