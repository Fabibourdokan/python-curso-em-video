for p in range(5):
    kg = float(input('Digite o peso da {}º pessoa: '.format(p+1)))
    if p == 0:
        maior = kg
        menor = kg
    else:
        if kg > maior:
            maior = kg
        if kg < menor:
            menor = kg
print('O maior peso lido foi {}kg'.format(maior))
print('O menor peso lido foi {}kg'.format(menor))

