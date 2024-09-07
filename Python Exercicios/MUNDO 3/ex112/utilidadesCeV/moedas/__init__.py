def moedas(num):
    return f'R${num:.2f}'


def metade(num, format=False):
    return num/2 if format is False else moedas(num/2)


def dobro(num, format=False):
    return float(num*2) if format is False else moedas(num*2)


def aumento(num, porcentagem, format=False):
    return num*(1+(porcentagem/100)) if format is False else moedas(num*(1+(porcentagem/100)))


def diminuir(num, porcentagem, format=False):
    return num*(1-(porcentagem/100)) if format is False else moedas(num*(1-(porcentagem/100)))


def resumo(num, pa, pd):
    print("-"*35)
    print(f'{'RESUMO DO VALOR':^35}')
    print("-"*35)
    print(f'Preço analisado: \t{moedas(num)}')
    print(f'Dobro do preço: \t{dobro(num, format=True)}')
    print(f'Metade do preço: \t{metade(num, format=True)}')
    print(f'{pa}% de aumento: \t{aumento(num, pa, format=True)}')
    print(f'{pd}% de redução: \t{diminuir(num, pd, format=True)}')
    print("-"*35)