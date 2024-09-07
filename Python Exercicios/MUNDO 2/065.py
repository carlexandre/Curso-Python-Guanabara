s = 0
c = 0
opc = 'S'
while opc=='S':
    num = int(input('\nDigite o valor de um número: '))
    s += num
    c+=1
    if c==1:
        maior = num
        menor = num
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
    opc = str(input('\nVocê deseja adicionar mais um número?\n\n[S]/[N]\n\nSua opção: ')).upper().strip()[0]
    while opc!='S' and opc!='N':
        opc = str(input('\nOPÇÃO INVÁLIDA!!!\n\nVocê deseja adicionar mais um número?\n\n[S]/[N]\n\nSua opção: ')).upper().strip()[0]
    if opc == 'N':
        break
print(f'\nVocê digitou {c} números\n\nA média dos valores dados é igual = {(s/c):.2f}\n\nO menor número informado foi: {menor}\n\nO maior número informado foi: {maior}')  