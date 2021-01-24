p = float(input('Informe seu peso:'))
a = float(input('Digite sua altura:'))
imc = p / pow(a, 2)
if imc == 18.5:
    print('Você está abaixo do peso! Seu peso é {:.2f}kg e seu imc é {:.2f}'.format(p, imc))
elif imc > 18.5 and imc <= 25:
    print('Você esta dentro do peso ideial!! Seu peso é {:.2f}kg e seu imc de {:.2f}'.format(p, imc))
elif imc > 25 and imc <= 30:
    print('Você esta acima do peso ideial!! Seu peso é {:.2f}kg e seu imc de {:.2f}'.format(p, imc))
elif imc > 30 and imc <= 40:
    print('Você esta obeso! Seu peso é de {:.2f}kg e seu imc de {:.2f}'.format(p, imc))
else:
    print('Você esta muiro acima do peso! Você tem obesidade mórbida. Seu peso é de {:.2f}kg e seu imc é de {:.2f}'.format(p, imc))

