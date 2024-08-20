a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))
if a+b>c and a+c>b and b+c>a:
    if a==b and b==c:
        print('Os segmentos acima podem formar um triângulo EQUILÁTERO.')
    elif a==b or a==c or b==c:
        print('Os segmentos acima podem formar um triângulo ISÓSCELES.')
    else: 
        print('Os segmentos acima podem formar um triângulo ESCALENO.') 
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')                  