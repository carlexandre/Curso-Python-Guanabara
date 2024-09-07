from time import sleep

def maior(*numeros):
    c = m = 0
    print('=-'*20)
    print('Analisando os números...')
    sleep(2)
    print('Os números analisados foram: ', end='')
    for i in numeros:
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
        c+=1
        if i>m:
            m=i
    sleep(1)
    print(f'\nTotal de Números: {c} | Maior número: {m}')


maior(4, 7, 0)
maior(2, 4)
maior(6)
maior()
print('=-'*20)