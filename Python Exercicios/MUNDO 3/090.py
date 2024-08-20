boletim = dict()
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input('Média: '))
if boletim['Média']<7:
    boletim['Situação'] = 'Reprovado'
else:
    boletim['Situação'] = 'Aprovado'
for i, j in boletim.items():
    print(f'{i}: {j}')