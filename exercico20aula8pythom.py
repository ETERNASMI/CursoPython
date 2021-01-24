import random
al1 = str(input('Digite o nome do 1 aluno:'))
al2 = str(input('Nome do aluno 2:'))
al3 = str(input('Nome do aluno 3:'))
al4 = str(input('Nome do alino 4:'))
al5 = str(input('Nome do alino 5:'))
st = [al1, al2, al3, al4, al5]
print('A ordem dos alunos sorteados é {}'.format(random.sample(st, k=5)))