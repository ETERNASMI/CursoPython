import random
al1 = str(input('Digite o nome do 1 aluno:'))
al2 = str(input('Nome do aluno 2:'))
al3 = str(input('Nome do aluno 3:'))
al4 = str(input('Nome do alino 4:'))
st = [al1, al2, al3, al4]
print('Nome do 1 aluno:{}'.format(al1))
print('Nome do 2 aluno:{}'.format(al2))
print('Nome do 3 aluno:{}'.format(al3))
print('Nome do 4 aluno:{}'.format(al4))
print('O aluno sorteado é {}'.format(random.choice(st)))
