s=0
co=0
for c in range(1, 501):
    if c%2!=0 and c%3==0:
        s+=c
        co+=1
        print(c)
print('A soma dos {} numeros de mutiplo de 3 é {}'.format(co, s))