import random 
alunos= str(input("Digite o nome dos alunos: "))
a1, a2, a3, a4 = alunos.split()
a1 = str(a1)
a2 = str(a2)
a3 = str(a3)
a4 = str(a4)
lista = [a1, a2, a3, a4]
sort = random.choice(lista)
print(f'O aluno escolhido foi: {sort}')