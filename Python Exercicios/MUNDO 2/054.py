c=0
for i in range(0,7):
    nome = str(input('Digite o nome da pessoa: '))
    ano = int(input('Digite o ano de nascimento dessa pessoa: '))
    pessoa = f'{nome} nasceu em {ano}'
    if (2024-ano>=21):
        print(f'{pessoa} e já atingiu a maioridade.\n')
        c+=1
    else:
        print(f'{pessoa} e ainda não atingiu a maioridade.\n')
print(f'{c} pessoa(s) JÁ atingiram a maioridade\n{7-c} pessoa(s) NÃO atingiram a maioridade.')        