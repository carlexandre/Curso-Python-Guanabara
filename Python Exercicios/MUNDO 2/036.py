valor = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário mensal? '))
anos = int(input('Quantos anos você deseja pagar essa casa? '))
prestm = valor/(anos*12)
if 0.3*sal<prestm:
    print(f'EMPRÉSTIMO NEGADO\nParcela mensal de {prestm:.2f} é maior que 30% do salário dado anteriormente.')
else: 
    print(f'EMPRÉSTIMO APROVADO\nCom parcela mensal no valor de R${prestm:.2f}')    