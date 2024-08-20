n = int(input('Digite quantos elementos da sequência de fibonacci você quer: '))
c=3
ant = 0
pen = 1
print(f'1° Termo: {ant}\n2° Termo: {pen}')
while c<=n:
    fib = ant + pen
    aux = pen
    pen = fib
    ant = aux
    print(f'{c}° Termo: {fib}')
    c+=1    