import math
ang = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(ang))
coss = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
if coss==6.123233995736766e-17 or coss==-1.8369701987210297e-16:
    print(f'O seno desse ângulo é: {sen:.2f} \nO cosseno desse ângulo é: {coss:.2f} \nA tangente desse ângulo não existe.')
else:
    print(f'O seno desse ângulo é: {sen:.2f} \nO cosseno desse ângulo é: {coss:.2f} \nA tangente desse ângulo é: {tang:.2f}')