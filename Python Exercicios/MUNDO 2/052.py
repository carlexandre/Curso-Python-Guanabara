num = int(input('Digite um número: '))
for i in range(2,num+1):
    if(num%i==0):
        if(i!=num):
            primo = "NÃO é PRIMO."
            break
        else:
            primo = "é PRIMO."
    else:
        primo = "é PRIMO."

print(f'O número {num} {primo}')        