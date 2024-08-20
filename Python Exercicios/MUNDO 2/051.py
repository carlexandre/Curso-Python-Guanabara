t1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão dessa PA: '))
c = 1
d = t1 + (10-1) * r
for i in range(t1, d+r, r):
    print(f'{c}° Termo da PA: {i}')
    c+=1