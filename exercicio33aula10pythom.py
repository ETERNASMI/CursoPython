n1 = float(input('Digite um numero:'))
n2 = float(input('Digite outro numero:'))
n3 = float(input('Digite mais outro numero:'))
if n1 > n2 and n1 > n3:
    print('O primeiro numero {} é o maior numero, comparados a {} e {}'.format(n1, n2, n3))
elif n2 > n1 and n2 > n3:
    print('O segundo numero {} é maior que {} e {}'.format(n2, n1, n3))
else:
    print('O terceiro numero {} é o maior numero comparado a {} e {}'.format(n3, n1, n2))
