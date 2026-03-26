km = float(input('Qual é a distância da viagem? '))
print('Você esta prestes a começar uma viagem de {}KM!'.format(km))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('O preço de sua passagem será de R${:.2f}'.format(preço))