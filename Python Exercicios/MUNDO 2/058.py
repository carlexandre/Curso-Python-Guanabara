from random import randint
print('REGRAS: Para ganhar o jogo você precisar acertar qual foi o número escolhido pelo computador dos números de 0 a 10!!')
numpc = randint(0,10)
num = int(input('\nDigite um número de 0 a 10: '))
c = 1
while num != numpc:
    c+=1
    if num>numpc:
        num = int(input('\nMenor!!! Digite novamente: '))
    if num<numpc:
        num = int(input('\nMaior!!! Digite novamente: '))    
if num == numpc:
    print(f'\nPARÁBENS VOCÊ GANHOU!!!\nO número escolhido pelo computador foi: {numpc}\nValor Total de Palpites: {c}')