def fatorial(num=1, show=False):
    f=1
    for i in range(num, 0, -1):
        f*=i
        if show:
            if i==1:
                print(f'{i} = ', end='')
            else:
                print(f'{i} x ', end='')
    return f
    
 
#main
n = int(input('\nDigite um número: '))
print(f'\nFatorial ({n}): ', end='')
print(fatorial(n, show=True))