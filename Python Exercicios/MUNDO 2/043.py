peso = float(input('Peso em kg: '))
altura = float(input('Altura em m: '))
imc = peso/(altura**2)
if imc <18.5:
    print(f'IMC: {imc:.1f}\nABAIXO DO PESO')
elif imc>=18.5 and imc<25:
    print(f'IMC: {imc:.1f}\nPESO IDEAL')    
elif imc>=25 and imc<30:
    print(f'IMC: {imc:.1f}\nSOBREPESO')
elif imc>=30 and imc<40:
    print(f'IMC: {imc:.1f}\nOBESIDADE')
else:
    print(f'IMC: {imc:.1f}\nOBESIDADE MÓRBIDA')    
                  