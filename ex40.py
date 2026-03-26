n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('A sua média foi {:.1f} você está REPROVADO'.format(m))
elif m >= 5 and m < 6.9:
    print('A sua média foi {:.1f} você está de RECUPERAÇÃO'.format(m))
else:
    print('A sua média foi {:.1f} você está APROVADO'.format(m))