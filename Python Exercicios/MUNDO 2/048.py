s=0
c =0
for i in range(3,500,3):
    if(i%2==1):
        s=s+i
        c+=1
print(f'O valor da soma dos {c} valores ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500 é igual a {s}')        