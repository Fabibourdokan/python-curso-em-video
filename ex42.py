a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos PODEM formar um triângulo.')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b or a == c or b == c:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos NÃO podem formar um triângulo')
