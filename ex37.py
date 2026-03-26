numero = int(input('Digite um número inteiro: '))
print('Escolha uma opção: ')
print('[ 1 ] converter para binário')
print('[ 2 ] converter para octal')
print('[ 3 ] converter para hexadecimal')
opção_usuario = int(input('Sua opção: '))
if opção_usuario == 1:
    print('{} convertido para binário é igual a: {}'.format(numero, bin(numero)))
elif opção_usuario == 2:
    print('{} convertido para octal é igual a: {}'.format(numero, oct(numero)))
elif opção_usuario == 3:
    print('{} convertido para hexadecimal é igual a: {}'.format(numero, hex(numero)))
