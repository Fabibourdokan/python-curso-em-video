soma_total = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulher = 0
for c in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper()
    soma_total += idade
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_mais_velho = nome
    if sexo == 'F' and idade < 20:
        mulher += 1
média = soma_total / 4
print('Média de idade: {}'.format(média))
print('O nome do homem mais velho é {}'.format(nome_mais_velho))
print('Têm {} mulheres com menos de 20 anos'.format(mulher))