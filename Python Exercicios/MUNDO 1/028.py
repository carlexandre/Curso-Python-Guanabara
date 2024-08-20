import random

print('O computador escolheu um número de 0 a 5, para vencer o jogo você deve escolher o mesmo número escolhido por ele.\n')
num = int(input("Digite um número de 0 a 5: "))
numcomp = random.randint(0,5)
if numcomp == num:
    print(f'Parabéns, você venceu!\n O computador também escolheu o número {num}.')
else:
    print(f'Poxa, você perdeu!\nO número escolhido pelo computador foi {numcomp}.')    
