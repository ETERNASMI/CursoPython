pn = float(input('Informe o preço do produto:'))
pg = int(input('Se o preço a pagar é a vista em dinheiro ou cheque digite:1\nSe o pagamento é no cartão a vista digite:2'
'\nSe é 2x no cartão digite:3\n3x ou mais no cartão digite:4\n'))
qc = int(input('Quantas vezes no cartão:'))
if pg == 1:
    p = (pn*10)/100
    pt = pn-p
    print('O preço a ser pago com desconto de 10% é R${:.2f}'.format(pt))
elif pg == 2:
    p = (pn*5)/100
    pt = pn-p
    print('O preço a ser pago com desconto de 5% éR${:.2f}'.format(pt))
elif pg == 3 and qc == 2:
    pt = pn
    print('Não a desconto o preço ha ser pago é R${:.2f}'.format(pt))
else:
    p = (pn*20)/100
    pt = pn+p
    pd = pt/qc
    print('O preço total a ser pago é de R${:.2f}, e em parcelas são R${:.2f} em {}x'.format(pt, pd, qc))
