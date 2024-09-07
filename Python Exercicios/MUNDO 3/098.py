from time import sleep

def contador(inicio, fim, passo):
    print('=-'*20)
    print(f'CONTAGEM DE {inicio} --> {fim} | {passo}')
    sleep(2)
    c=inicio
    if passo>0:
        while c<=fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c+=passo
    else:
        while c>=fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c+=passo
    print('FIM!!!')
    print('=-'*20)
   

contador(1, 10, 1)
contador(10,0,-2)
print('Agora é sua vez de escolher a contagem!!!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)