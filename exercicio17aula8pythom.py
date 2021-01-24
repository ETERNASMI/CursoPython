from math import pow
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor catelo adjacente:'))
hp = pow(co, 2) + pow(ca, 2)
print('O cateto oposto é {}, cateto adjacente é {} e o valor da hipotenusa é {}'.format(co, ca, hp))