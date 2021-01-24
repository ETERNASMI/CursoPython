co=0
me=0
ma=0
for c in range(1, 5):
    n = input('Digite sue nome:')
    i = int(input('Informe sua idade:'))
    s = str(input('Informe seu genero M - masculino e F - feminino:'))
    me += i
    m = me/c
    if i > ma:
        ma = i
        no = n
    if s == 'F' and i < 20:
        co+=1
print('A media de idade é {}'.format(m))
print('o nome da pessoa com maior idade é {} com {}anos'.format(no, ma))
print('O numero de mulheres menor de 20 anos são {}'.format(co))