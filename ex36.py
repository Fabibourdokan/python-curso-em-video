'''valor = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
parcelas = anos * 12
print('você pagará {} parcelas'.format(parcelas))
prestação = valor / parcelas
print('O valor de cada parcela será de R${:.2f}'.format(prestação))
limite = salario * 30 / 100
print('O limite que você tem aprovado para pagar por parcela é de R${:.2f}'.format(limite))
if prestação > limite:
    print('O seu emprestimo foi negado!')
else:
    print('O seu emprestimo foi aprovado!')'''


casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o saláio do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')