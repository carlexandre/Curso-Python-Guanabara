import moedas

valor = float(input('Digite o valor: R$'))

print(f'A metade de {moedas.moedas(valor)} é {moedas.metade(valor, format=True)}')
print(f'O dobro de {moedas.moedas(valor)} é {moedas.dobro(valor, format=True)}')
print(f'Aumentando 10%, temos {moedas.aumento(valor, 10, format=True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(valor, 13, format=True)}')