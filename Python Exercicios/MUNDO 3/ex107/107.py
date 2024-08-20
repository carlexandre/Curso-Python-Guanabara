import moedas

valor = float(input('Digite o valor: R$'))

print(f'A metade de {valor} é {moedas.metade(valor)}')
print(f'O dobro de {valor} é {moedas.dobro(valor)}')
print(f'Aumentando 10%, temos {moedas.aumento(valor, 10)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(valor, 13)}')