te = str(input('Digite uma frase:')).strip().lower()
print('A letra a aparece {} vezes'.format(te.count('a')))
print('esta é a primeira possição em que a letra a aparece {}'.format(te.find('a')+1))
print('Esta é a ultiva posição em que a letra a aparece {}'.format(te.rfind('a')+1))