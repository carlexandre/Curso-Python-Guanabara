from time import sleep


def titulo(frase):
    print("-"*45)
    print(f'{frase:^45}')
    print("-"*45)


def menuescolha(frase):
    while True:
        try:
            n = int(input(frase))
        except (ValueError, TypeError):
            print('ERRO: Digite um valor válido.')
            continue
        else:
            if n<1 or n>3:
                print('ERRO: Digite um valor válido.')
            else:
                break
    return n


def cadastro():
    titulo('NOVO CADASTRO')
    with open('pessoascadastradas.txt', 'a') as arquivo:
        n = input('Nome: ').strip()
        if n=='':
            n='Desconhecido'
        arquivo.write(n)
        arquivo.write(';')
        s = input('Idade: ')
        while not s.isnumeric():
            print('ERRO: Digite um valor válido.')
            s = input('Idade: ')
        arquivo.write(s)
        arquivo.write(' anos')
        arquivo.write('\n')
        print(f'Cadastro de {n} concluído.')


def mostrarcadastro():
    titulo('PESSOAS CADASTRADAS')
    with open('pessoascadastradas.txt', 'r') as arquivo:
        cadastros = arquivo.readlines()
    
    if len(cadastros)==0:
        print(f'{'Não há nenhum cadastro. Cadastre uma pessoa.':^45}')
    for j in cadastros:
        nome, idade = j.split(';')
        idade = idade.replace('\n','')
        print(f'{nome:<35} {idade:>2}')


def hall(num):
    if num==1:
        sleep(0.5)
        mostrarcadastro()
        sleep(0.3)
    elif num==2:
        sleep(0.5)
        cadastro()
        sleep(0.3)
    else:
        sleep(0.5)
        titulo("FINALIZANDO PROGRAMA...")
        sleep(0.3)
        sn=0
        return sn
