from random import randint
from time import sleep

def sorteio(quantidade, lista):
    print('Números sorteados: ', end='')
    for i in range(0,quantidade):
        sleep(0.5)
        n = randint(0,9)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    print()


def somapares(lista):
    s=0
    pares = list()
    for i in lista:
        if i%2==0:
            s+=i
            pares.append(i)
    for i in range(0,len(pares)):
        sleep(0.5)
        if i==len(pares)-1:
            print(f'{pares[i]} = ', end='')
        else:
            print(f'{pares[i]} + ', end='', flush=True)
    sleep(0.5)
    print(f"{s}")


numeros=list()
sorteio(10, numeros)
somapares(numeros)