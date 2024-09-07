frase = str(input('Digite uma frase qualquer: ')).strip()
print(f'A letra A aparece {frase.upper().count('A')} vezes')
print(f'A letra A aparece na posição {frase.upper().find('A')+1} pela primeira vez')
print(f'A letra A aparece na posição {frase.rfind('A')+1} pela última vez')