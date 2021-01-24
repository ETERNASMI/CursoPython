d = float(input('Digite a distancia da sua viagem:'))
if d <= 200:
    p = 0.50*d
    print('O preço para essa distancia é R${:.2f}'.format(p))
else:
    p = 0.45*d
    print('O preço para distancia maiores que 200km o valor é de R${:.2f}'.format(p))
