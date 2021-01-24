ma = 0
me = 999
for c in range(1, 6):
    p = float(input('Informe seu seu peso:'))
    if p > ma:
        ma = p
    if p < me:
        me = p
print('o maior peso é {}kg'.format(ma))
print('O menor peso é {}kg'.format(me))