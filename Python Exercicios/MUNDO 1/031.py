km = int(input('Digite a distância da viagem que irá fazer: '))
if km<=200:
    valor = 0.5*km
    print(f'O valor da passagem para a viagem desejada é R${valor:.2f}')
else:
    valor = 0.45*km
    print(f'O valor da passagem para a viagem desejada é R${valor:.2f}')    