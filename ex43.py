peso = float(input("Digite o seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("O seu IMC é {:.2f} e está abaixo do peso".format(imc))
elif imc >= 18.5 and imc < 25:
    print('O seu IMC é {:.2f} e você está no peso ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('O seu IMC é {:.2f} e você está com sobrepeso'.format(imc))
elif imc >= 30 and imc < 40:
    print('O seu IMC é {:.2f} e você esta com obesidade'.format(imc))
else:
    print('O seu IMC é {:.2f} e você está com obesidade mórbida'.format(imc))