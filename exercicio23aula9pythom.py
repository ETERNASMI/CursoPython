num = int(input('digite um numero de 0 a 9999:'))
#n = str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Numero analisado {}'.format(num))
print('Milhar:{}'.format(m))
print('Centena:{}'.format(c))
print('Decimal:{}'.format(d))
print('Unidade:{}'.format(u))