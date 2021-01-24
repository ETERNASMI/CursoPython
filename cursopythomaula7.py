#ordem de precendencia
#1=().2=**.3=*,/,//,%.4=+,-
# {:.3f}numero so com 3 casa decimais depois da virgula end='  ' nao pula o print
n = input('qual é o seu nome?\n')
print('Prazer em te conhecer {:=^10}!'.format(n))
n1 = int(input('Deu um valor: '))
n2 = int(input('Deuso 2 valor: '))
print('A soma vale: {}'.format(n1+n2))
print('Divisao é {:.3f}'.format(n1/n2))
