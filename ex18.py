from math import radians, sin, cos, tan
angulo = float(input("Digite o angulo: "))
seno = sin(radians(angulo))
print('O angulo {} tem o valor {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('o angulo {} tem o valor {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo {} tem o valor {:.2f}'.format(angulo, tangente))
