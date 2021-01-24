n = int(input('Digite um numero inteiro:'))
#if n/n and n/1 and n % 2 != 0:
#    print('Este numero  é primo', n)
#elif n == 2:
#    print('{} é primo'.format(n))
#else:
 #   print('Este numero nao  é primo', n)
c = 0

for x in range(2, n):
    if n % x == 0:
        print("Este numero não é primo", n)
        c += 1

if c == 0:
    print("É primo")
else:
    print("Tem",c," múltiplos acima de 2 e abaixo de",n)