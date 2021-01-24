vt = float(input('De um valor:'))
vt2 = float(input('Um segundo valor:'))
vt3 = float(input('O ultimo valor:'))
if vt < vt2 + vt3 and vt> abs(vt2-vt3):
    if vt == vt2 and vt == vt3:
        print('É possivel formar um triangulo do tipo EQUILATERO!!\nSendo que seus lados são {:.2f}, {:.2f} e {:.2f}'.format(vt, vt2, vt3))
    elif vt == vt2:
        print('É possivel formar um triangulo do tipo ISOSCELES!!\nSendo que seus lados são {:.2f}, {:.2f} e {:.2f}'.format(vt, vt2, vt3))
    elif vt == vt3:
        print('É possivel formar um triangulo do tipo ISOSCELES!!\nSendo que seus lados são {:.2f}, {:.2f} e {:.2f}'.format(vt, vt2, vt3))
    elif vt2 == vt3:
        print('É possivel formar um triangulo do tipo ISOSCELES!!\nSendo que seus lados são {:.2f}, {:.2f} e {:.2f}'.format(vt, vt2, vt3))
    elif vt != vt2 and vt != vt3 and vt2 != vt3:
        print('É possivel formar um triangulo do tipo ESCALENO!!\nSendo que seus lados são {:.2f}, {:.2f} e {:.2f}'.format(vt, vt2, vt3))
else:
    print('Com estes valores {:.2f}, {:.2f} e {:.2f} não é posivel formar nenhum tipo de triangulo!!'.format(vt, vt2, vt3))