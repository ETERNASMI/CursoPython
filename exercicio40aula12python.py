nt = float(input('Digite sua primeira nota:'))
nt2 = float(input('Digite sua outra nota:'))
m = (nt + nt2) / 2
if m < 5.0:
    print('Sua media esta abaixo da media, sua media é {:.2f}'.format(m))
    print('Você foi Reprovado!')
elif m == 5.0 or m <= 6.9:
    print('Você esta na media, sua media é de {:.2f}'.format(m))
    print('Você esta na Recuperação!!')
else:
    print('Você esta acima da media, sua media é de {:.2f}'.format(m))
    print('Parabéns!!! Você foi APROVADO!!')
