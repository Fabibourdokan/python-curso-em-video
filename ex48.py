soma = 0
contador = 0
for n in range(1, 501):
    if n % 3 == 0 and  n % 2 != 0:
        soma += n
        contador += 1
print('A soma de todos os {} valores solicitados é {}'.format(contador, soma))