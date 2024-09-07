def notas(*n, sit=False):
    analise = dict()
    analise["Total"] = len(n)
    maior=0
    menor=10
    s=0
    for i in n:
        s+=i
        if i<menor:
            menor = i
        if i>maior:
            maior = i
    analise['Maior Nota'] = maior #analise['Maior Nota'] = max(n)
    analise['Menor Nota'] = menor #analise['Menor Nota'] = min(n)
    analise['Média'] = s/analise['Total'] #analise['Média'] = sum(n)/len(n)
    if sit:
        if analise['Média']>=7:
            analise['Situação'] = 'Boa'
        elif analise['Média']<=5:
            analise['Situação'] = 'Ruim'
        else:
            analise['Situação'] = 'Razoável'
    return analise


#main
resp = notas(5.5, 3, 10, 6.5, 10)
print(resp)