l1 = float(input('Digite o primeiro lado:'))
l2 = float(input('Digite o segundo lado:'))
l3 = float(input('Digite o terceiro lado:'))
if l1 < l2 + l3 and l1 > abs(l2-l3):
    print('É possivel formar um triangulo com esses valores {},{}, {}'.format(l1, l2, l3))
else:
    print('Não é possivel formar um triangulo com esses valores {}, {}, {}'.format(l1, l2, l3))

