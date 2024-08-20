num = int(input("Digite o número que você quer converter? "))
escolha = int(input('Escolha qual será a base de conversão: \n[1]BINÁRIO\n[2]OCTAL\n[3]HEXADECIMAL\nSua opção: '))
if escolha == 1:
    print(f'O número {num} convertido para binário é: {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} convertido para binário é: {oct(num)[2:]}') 
elif escolha == 3:
    print(f'O número {num} convertido para binário é: {hex(num).upper()[2:]}')
else:
    print('OPÇÃO INVÁLIDA.')         
