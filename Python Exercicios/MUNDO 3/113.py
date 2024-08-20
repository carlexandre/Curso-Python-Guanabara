def leiaint(frase):
    while True:
        try:
            num = int(input(f'\n{frase}'))
        except (ValueError, TypeError):
            print('\nERRO: Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número.')
            num=0
        else:
            break
    return num


def leiafloat(frase):
    while True:
        try:
            num = float(input(f'\n{frase}'))
        except (ValueError, TypeError):
            print('\nERRO: Digite um número real válido.')
        except KeyboardInterrupt:
            print('\nUsuário preferiu não digitar esse número.')
            num=0
        else:
            break
    return num


#main
inteiro = leiaint('Digite um inteiro: ')
flutuante = leiafloat('Digite um real: ')
print(f'\nVocê digitou o inteiro {inteiro} e o real {flutuante}.\n')
