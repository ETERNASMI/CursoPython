c1 = 0
c2 = 0
for c in range(1, 8):
    a = int(input('Digite sua idade:'))
    if a >= 21:
           c1+=1
           print('Você já é maior de idae e tem {}anos'.format(a))
    else:
           c2+=1
           print('Você é menor de idade e sua idade é {}anos'.format(a))
print('O numero de pessoa maior de idade são {}'.format(c1))
print('O numero de pessoa menor de idade são {}'.format(c2))