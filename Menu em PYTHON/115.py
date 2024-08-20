import modulo

flag = 1
while True:
    modulo.titulo('MENU PRINCIPAL')
    print(f'1 - Ver Pessoas Cadastradas\n2 - Cadastrar Nova Pessoa\n3 - Sair do Sistema')
    print('-'*40)
    t = modulo.menuescolha('Sua Opção: ')
    flag = modulo.hall(t)
    if flag==0:
        break