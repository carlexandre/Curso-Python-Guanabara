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