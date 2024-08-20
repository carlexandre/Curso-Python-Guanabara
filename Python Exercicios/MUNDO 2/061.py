t1 = int(input('\nDigite o primeiro termo da PA: '))
r = int(input('\nDigite a razão dessa PA: '))
print()
c = 1
while c<=10:
    d = t1 + (c-1) * r
    print(f'{c}° Termo: {d}')
    c+=1