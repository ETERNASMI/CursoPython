s = 0
for c in range(1, 7):
    n = int(input('Digite um numero:'))
    #print(n)
    if n % 2 == 0:
       s += n
print('a soma dos numeros par é {}'.format(s))
if s == 0:
   print('Todos os numeros sao impares')
