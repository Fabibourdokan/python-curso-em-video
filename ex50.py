soma = 0
for c in range(6):
    n = int(input('Digite o {}º valor: '.format(c+1)))
    if  n % 2 == 0:
        soma += n
print('A soma dos valores pares é {}'.format(soma))