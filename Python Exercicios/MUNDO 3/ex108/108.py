import moedas

valor = float(input('Digite o valor: R$'))

print(f'A metade de {moedas.moedas(valor)} é {moedas.moedas(moedas.metade(valor))}')
print(f'O dobro de {moedas.moedas(valor)} é {moedas.moedas(moedas.dobro(valor))}')
print(f'Aumentando 10%, temos {moedas.moedas(moedas.aumento(valor, 10))}')
print(f'Reduzindo 13%, temos {moedas.moedas(moedas.diminuir(valor, 13))}')