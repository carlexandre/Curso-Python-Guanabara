from time import sleep 
si=0
maior=-1
c=0
for i in range(0,4):
    nome = str(input(f'\nDigite o nome da {i+1}° pessoa: ')).strip()
    sleep(0.1)
    idade = int(input(f'Digite a idade da {i+1}° pessoa: '))
    sleep(0.1)
    sexo = int(input(f'Selecione o sexo da {i+1}° pessoa:\n[1] MASCULINO\n[2] FEMININO\nDigite sua opção: '))
    sleep(0.1)
    si=idade+si
    if(sexo == 1):
        if(idade>maior):
            nomemaior = nome
            maior = idade
    if(sexo == 2):
        if(idade<20): c+=1  
sleep(1)             
print(f'\nA média de idade do grupo informado é de {(si/4):.2f} anos.\n')
print(f'{nomemaior} é o nome do homem mais velho com {maior} anos.\n')
print(f'O número de mulheres que têm menos de 20 anos é igual a {c}\n')
