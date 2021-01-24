vs = float(input('Qual é o seu salrio?\n'))
if vs > 1250.00:
    s = vs*10/100
    ns = vs + s
    print('Seu salario com um aumento de 10% será R${:.2f}'.format(ns))
else:
    s = vs*15/100
    ns = vs + s
    print('O seu salario com aumento de 15% é R${:.2f}'.format(ns))
