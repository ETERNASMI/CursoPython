v = int(input('Qual é a velocidade do carro?\n'))
if v > 80:
    m = float(7.00*(v-80))
    print('MULTADO! Você excedeu o limete de 80Km/h')
    print('Sua velocidade esta acima da velocidade maxima permitida, você foi multado em R${:.2f}'.format(m))
else:
    print('Sua velocidade é de {:.2f}km/h'.format(v))
    print('Dirija com segurança!')
