nl = input('Digite um numero inteiro: ')
v = int(input('Qual base você deseja converter? 1- Binario; 2- Octal e 3- Hexadecimal: '))
n = int(nl)

nb = ''
while n > 0:

     if v == 1:
         cb = bin(n)
         print('coversao binario', cb[2:])

         if n % 2 == 0:
                n = int(n/2)
                #nr = 1
                print('resto é:', 0, end='')
                #nb += '0'
         elif n % 2 == 1:
                n = int(n/2)
                #nr = 1
                print('resto é:', 1, end ='')
                #nb += '1'
     if v == 2:
         co = oct(n)
         print('conversao oc', co[2:1])
     elif v == 3:
         ch = hex(n)
         print('conversao hex', ch)[2:1]





   #nbi = nb[::-1]
   #if int(nl) > 0:
   # assert '0b' + nb == bin(int(nl))
# p = int(n/8)
# n = int(n % 8)
# print('sobra é:', p, n)
# def nh(n):
# if n>= 16:
# if n < 0:
# print(0),
# elif n<=1:
# print(n)
# else:
# p = int(n/16)
# x = int(n % 16)
# if x < 10:
##  print(n),
# if x == 10:
#  print('A'),
# if x == 11:
#    print('B'),
# if x == 12:
#   print('C'),
# if x == 13:
#   print('D'),
# if x == 14:
#   print('E'),
# if x == 15:
#   print('F'),

# nh(n / 16)