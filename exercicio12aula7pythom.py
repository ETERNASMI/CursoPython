pro = input('Digite o nome do produto: ')
p = float(input('Preço do produto: '))
d = (p*5)/100
pn = p - d
print('{} custa {} reais e o seu preço com desconto de 5% é {} reais'.format(pro, p, pn))
