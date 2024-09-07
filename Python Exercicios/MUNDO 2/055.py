for i in range(0,5):
    peso = float(input(f"\nDigite o peso da {i+1}° pessoa em kg: "))
    if i==0:
        maior = peso
        menor = peso
    elif peso>maior:
        maior = peso
    elif peso<menor:
        menor = peso
print(f'\nO maior peso é {maior:.1f}kg\nO menor peso é {menor:.1f}kg')            