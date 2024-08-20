from time import sleep

def ajuda(cmnd):
    titulo(f'Carregando o manual para a função ou biblioteca {cmnd}...')
    help(cmnd)

def titulo(msg):
    tam = len(msg) + 4
    print('='*tam)
    print(f'  {msg}')
    print('='*tam)
    sleep(1.5)


#main
comando=''
while True:
    titulo('Sistema de Ajuda PYHELP')
    comando=str(input('Função ou Biblioteca: '))
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)
titulo('Encerrando o Programa... ')