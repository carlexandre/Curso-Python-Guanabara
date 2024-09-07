numbers = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
cont = 'S'
while cont=='S':
    num = int(input('\nDigite um número entre 0 e 20: '))
    while num>20 or num<0:
        num = int(input('\nDigite um número entre 0 e 20: '))
    print(f'\nVocê digitou o número {numbers[num]}.')
    cont = str(input('\nVocê quer continuar? [S] [N]\nSua Opção: ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('\nVocê quer continuar? [S] [N]\nSua Opção: ')).strip().upper()
