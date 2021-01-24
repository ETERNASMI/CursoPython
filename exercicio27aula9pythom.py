no = str(input('Digite seu nome completo:')).strip()
pno = no.split()
print('Seu primeiro nome é {}'.format(pno[0]))
print('Seu ultimo nome é {}'.format(pno[len(pno)-1]))
