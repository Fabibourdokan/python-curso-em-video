palavra = str(input('Digite uma palavra/frase: ')).strip().upper().replace(' ','')
if palavra == palavra[::-1]:
    print('A palavra/frase {} de trás para frente é {}, portanto é um palíndromo.'.format(palavra, palavra[::-1]))
else:
    print('A palavra/frase {} de trás para frente é {}, portanto NÃO é um palíndromo.'.format(palavra, palavra[::-1]))