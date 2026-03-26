n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O {} é maior que o {}'.format(n1, n2))
elif n2 > n1:
    print('O {} é maior que o {}'.format(n2, n1))
else:
    print('NÃO exite número maior, {} e {} são iguais!'.format(n1, n2))