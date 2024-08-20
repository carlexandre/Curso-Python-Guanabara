cont = 0
while True:
    num = int(input("\nDigite o número da tabuada: "))
    if num<0:
        print('Progama Encerrado.')
        break
    for i in range(1,11):
        print(f'{i} x {num} = {i*num}')