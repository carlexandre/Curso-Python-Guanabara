def area(larg, comp):
    print(f'A área de um terreno {larg:.1f} x {comp:.1f} é de {(larg*comp):.1f}m².')


print('\nControle de Terrenos\n')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print()
area(l, c)