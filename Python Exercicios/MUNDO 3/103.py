def jogador(nomejogador="<desconhecido>", golsfeitos=0):
    if nomejogador=='':
        nomejogador='<desconhecido>'
    if golsfeitos.isnumeric():
        golsfeitos=int(golsfeitos)
    else:
        golsfeitos=0
    return f'O jogador {nomejogador} fez {golsfeitos} gols no campeonato.'


#main
nome = input('\nNome do Jogador: ').strip()
gols = input('Número de Gols: ')
print()
print(jogador(nome, gols))
print()