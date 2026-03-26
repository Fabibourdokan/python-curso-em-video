soma = 0
termo = int(input('Digite um número: '))
razão = int(input('Digite a sua progressão: '))
for c in range(10):
    print('{}'.format(termo), end=' ')
    termo += razão
