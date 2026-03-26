from time import sleep
n = int(input('Me diga um número qualquer: '))
resultado = n % 2
print('PROCESSANDO...')
sleep(1)
if resultado == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é IMPAR'.format(n))