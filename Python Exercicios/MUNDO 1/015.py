dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos quilômetros foi rodado nesse carro? '))
total = 60*dias + km*0.15
print(f'O total a ser pago é R${total:.2f}')