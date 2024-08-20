valor = int(input('Digite o valor que você quer sacar: R$'))
n50 = valor//50
n20 = valor%50//20
n10 = valor%50%20//10
n1 = valor%50%20%10//1
f50=''
f20=''
f10=''
f1=''
if n50!=0:
    f50 = f'\nTotal de {n50} nota(s) de 50 reais.10'
if n20!=0:
    f20 = f'\nTotal de {n20} nota(s) de 20 reais.'
if n10!=0:
    f10 = f'\nTotal de {n10} nota(s) de 10 reais.'   
if n1!=0:
    f1 = f'\nTotal de {n1} nota(s) de 1 real.'
print(f'{f50}{f20}{f10}{f1}\n')             