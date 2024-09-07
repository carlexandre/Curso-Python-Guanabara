def leiaint(frase):
    num = input(f'\n{frase}')
    while not num.isnumeric():
        print('\nERRO! Digite um número inteiro válido.')
        num = input(frase)
    return num


#main
n = leiaint('Digite um número: ')
print(f'\nVocê digitou o número {n}.\n')
