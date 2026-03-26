preço = float(input('Qual o preço do produto? R$'))
print('FORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] Até 2x no cartão')
print('[4] 3x ou mais no cartão')
opcao = int(input('Escolha a opção de pagamento: '))
if opcao == 1:
    print('O valor da sua compra terá um desconto de 10%, o valor total já com desconto é R${:.2f}'.format(preço - (preço * 0.10)))
elif opcao == 2:
    print('O valor da sua compra terá um desconto de 5%, o valor total já com o desconto é R${:.2f}'.format(preço - (preço * 0.05)))
elif opcao == 3:
    print('O valor da sua compra parcelada será 2x de R${:.2f}.'. format(preço / 2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preço + (preço * 0.20)
    valor_parcelas = total / parcelas
    print('A sua compra parceladada em {}x sairá o preço de R${:.2f} por parcela, totalizando R${:.2f} COM JUROS'.format(parcelas, valor_parcelas, total))
else:
    print('Opção inválida, tente novamente com as opções 1, 2, 3 ou 4')