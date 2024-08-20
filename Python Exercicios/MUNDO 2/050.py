s=0
c=0
for i in range(0,6):
    num = int(input(f'Digite o {i+1}° número: '))
    if(num%2==0):
        s=s+num
        c+=1
print(f'A soma dos {c} números pares é {s}')        