from datetime import date
d = int(input('Digite o ano do seu nascimento:'))
c = date.today().year
a = c - d #int(date - d)
if a < 18:
    print('Você ainda não tem idade pára se alistar, sua idade é {}'.format(a))
    f = 18 - a
    print('Falta ainda {} anos para o você poder se alistar'.format(f))
elif a == 18:
    print('Você já tem idade para se alistar, sua idade é {} anos'.format(a))
else:
    print('Já passoua o idade de alistamento, sua idade é de {} anos'.format(a))
    f = a - 18
    print('passou {} anos depois da idade de alistamento'.format(f))
