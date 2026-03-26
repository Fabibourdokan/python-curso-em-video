salario = float(input('Qual o salario do funcionário?R$'))
if salario <= 1250:
    salario = salario + (salario * 15 / 100)
else:
    salario = salario + (salario * 10 / 100)
print('O valor do salário do funcionário com reajuste é de {:.2f}'.format(salario))