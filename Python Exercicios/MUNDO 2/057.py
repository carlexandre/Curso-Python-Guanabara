sexo = str(input('Escolha o sexo:\n[M]/[F]\nSua Opção: ')).upper().strip()
while sexo!='M' and sexo!='F':
    sexo = str(input('\nOpção Inválida! Tente novamente.\nEscolha o sexo:\n[M]/[F]\nSua Opção: ')).upper().strip()
if sexo == 'M':
    print('\nA pessoa é do sexo masculino.')
if sexo == 'F':
    print('\nA pessoa é do sexo feminino.')

    