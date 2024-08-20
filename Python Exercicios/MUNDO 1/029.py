km = int(input('Digite a velocidade do carro: '))
if km>80:
    multa = 7*(km-80)
    print(f'Você ultrapassou o limite estabelecido na via, o valor da multa a ser paga é R${multa}.')
else:
    print(f'Você não ultrapassou o limite estabelecido na via. Parabéns!')    