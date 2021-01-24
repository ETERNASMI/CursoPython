#from datetime import date
dn = int(input('Qual o ano que quer analisar? Ou se quer saber se o ano atual é bissexto digite 1\n'))
if dn % 4 == 0 and dn % 100 != 0 or dn % 400 == 0:
    print('{} é um ano bissexto'.format(dn))
#elif dn == 1:
else:
    print('{} não é um ano bissexto'.format(dn))
