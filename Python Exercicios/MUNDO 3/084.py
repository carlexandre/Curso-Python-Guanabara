pessoa = list()
pp = list()
nmai = list()
nmen = list()
c = 1
while True:
    pessoa.append(str(input('\nNome: ')))
    pessoa.append(float(input('Peso: ')))
    pp.append(pessoa[:])
    sn = str(input('\nVocê deseja continuar? [S]/[N]\nSua Opção: ')).upper().strip()
    while sn not in 'SN':
        sn = str(input('\nVocê deseja continuar? [S]/[N]\nSua Opção: ')).upper().strip()
    if sn == 'N':
        break
    elif sn == 'S':
        pessoa.clear()
        c+=1
for i in pp:
    if i[1]==pp[0][1]:
        maior = menor = i[1]
    if i[1]>maior:
        maior = i[1]
    if i[1]<menor:
        menor = i[1]

for i in pp:
    if i[1]==maior:
        nmai.append(i[0])
    if i[1]==menor:
        nmen.append(i[0])

print(f'\nVocê cadastrou {c} no total.\nO maior peso foi de {maior:.1f} kg. Peso de {nmai}.\nO menor peso foi de {menor:.1f} kg. Peso de {nmen}.')