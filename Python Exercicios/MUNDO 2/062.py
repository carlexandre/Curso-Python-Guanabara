t1 = int(input('\nDigite o primeiro termo da PA: '))
r = int(input('\nDigite a razão dessa PA: '))
opc = 'S'
n = 1
while opc == 'S' and n!=0:
    if opc == 'S':
        n = int(input('\nDigita a quantidade de termos da PA: '))
        print()
    c = 1
    if n!=0:
        while c<=n:
            d = t1 + (c-1) * r
            print(f'{c}° Termo: {d}')
            c+=1
        opc = str(input('\nDeseja mudar a quantidade de termos?\n\n[S]/[N]\n\nSua Opção: ')).upper().strip()
        if opc == 'N':
            break
