num = int(input('\nDigite o número que você deseja saber o fatorial: '))
c = 1
fat = num 
while c<num:
    fat = fat*c
    print(f'{num-(c-1)} x ', end='')
    c+=1
print(f'1 = {num}! = {fat}')    