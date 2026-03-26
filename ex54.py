from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(7):
    ano = int(input('Digite o ano de seu nascimento: '))
    idade = atual - ano
    print('Essa pessoa tem {} anos.'.format(idade))
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('De acordo com o ano de nascimento informado, tem {} pessoas maiores de idade e {} pessoas menosres de idade.'.format(maiores, menores))
