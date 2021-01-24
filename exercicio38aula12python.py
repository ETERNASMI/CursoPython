n1 = int(input('Digite um numero inteiro:'))
n2 = int(input('Outro numero inteiro:'))
if n1 > n2:
    print('o primeiro é maior! {} maior comparado que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo numero é maior. {} é maior comprado que {}'.format(n2, n1))
else:
    print("Os dois numero são iguais {} é igual a {}".format(n1, n2))
