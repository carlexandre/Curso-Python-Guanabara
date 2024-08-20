brt = 0
mdm = 0
erro=0
t = 0
while True:
    if erro==0:
        print('\nLOJA\n')
        nome = str(input('Nome do Produto: '))
        val = float(input('Valor do Produto: R$'))
        choic = str(input("Deseja continuar? [S]/[N]: ")).upper().strip()
        dc=1
    if erro==1:
        choic = str(input("Deseja continuar? [S]/[N]: ")).upper().strip()
    if t==0:
        brt = val
        nbrt = nome
    if val<brt and dc==1:
        brt = val
        nbrt = nome  
    if dc ==1:
        t = t+val
    if val>1000 and dc==1:
        mdm+=1
    if choic == 'N':
        print(f'\nProdutos com valores maiores que R$1.000: {mdm}\nProduto mais barato: {nbrt} - R${brt:.2f}\nTotal da compra: R${t:.2f}\n\nPrograma Encerrado')
    elif choic == 'S':
        erro=0
        continue
    else:    
        erro=1
        dc=0