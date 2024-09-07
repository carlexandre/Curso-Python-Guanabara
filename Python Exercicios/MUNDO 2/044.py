valor = float(input('VALOR DA COMPRA: '))
formap = int(input("FORMAS DE PAGAMENTO\n[1] À VISTA DINHEIRO/CHEQUE\n[2] À VISTA CARTÃO\n[3] 2x NO CARTÃO\n[4] 3x OU MAIS NO CARTÃO\nQUAL É A OPÇÃO? "))
if formap == 1:
    valorf= 0.9*valor 
    print(f'A COMPRA DE R${valor:.2f} FICA POR R${valorf:.2f} COM DESCONTO.')
elif formap == 2:
    valorf=0.95*valor
    print(f'A COMPRA DE R${valor:.2f} FICA POR R${valorf:.2f} COM DESCONTO.')
elif formap == 3:
    valorf=valor
    print(f'VALOR A SER PAGO: R${valorf:.2f}')
elif formap == 4:
    parc = int(input('QUANTIDADES DE PARCELA: '))
    valorf = 1.2*valor
    valorp = valorf/parc
    print(f'VALOR TOTAL COM JUROS: R${valorf:.2f}\nVALOR DA PARCELA MENSAL: R${valorp:.2f}')
else:
    print('OPÇÃO INVÁLIDADE DE PAGAMENTO.\nTENTE NOVAMENTE.')
