from datetime import date
c = date.today().year
ida = int(input('Digite o ano do seu nascimento:'))
ct = c - ida
if ct <= 9:
    print('Você tem {} anos'.format(ct))
    print('Sua categoria é MIRIM!')
elif ct <= 14:
    print('Você tem {} anos'.format(ct))
    print('Você pertence a categoria INFANTIL!')
elif ct <= 19:
    print('Você tem {} anos'.format(ct))
    print('Sua categoria é JUNIOR')
elif ct ==20:
    print('Você tem {} anos'.format(ct))
    print('Sua categoria é SENIOR!!')
else:
    print('Você tem {} anos'.format(ct))
    print('Você já é da categoria MASTER!!')
