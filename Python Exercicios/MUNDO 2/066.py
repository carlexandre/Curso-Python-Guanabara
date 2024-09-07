num = 0
s = 0
c = 0
while True:
    num = int(input('\nDigite o valor de um número | [999] para PARAR: '))
    if num == 999:
        break
    s = num + s
    c+=1
print(f'\nTotal de números digitados: {c}\n\nA soma desses números foi: {s}\n')