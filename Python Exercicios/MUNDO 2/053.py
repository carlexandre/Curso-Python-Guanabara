plvr = str(input('Digite uma frase: ')).strip()
plvr = plvr.replace(' ','').upper()
plvr.split()
tam = len(plvr)
for i in range(0,tam,2):
    if plvr[0+i]==plvr[tam-1-i]:
        resp = 'é um PALÍNDROMO.'
    else:
        resp = 'NÃO é um PALÍNDROMO.'            
print(f'Essa frase {resp}')