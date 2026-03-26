from datetime import date
ano_nasc = int(input('Qual o ano de nascimento? '))
idade = date.today().year - ano_nasc
if idade <= 9:
    print('O atleta tem {} anos, e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos, e esta na categoria JÚNIOR.'.format(idade))
elif idade <= 20:
    print('O atleta tem {} anos, e esta na categoria SÊNIOR.'.format(idade))
else:
    print('O atleta tem {} anos, e esta na categoria MASTER.'.format(idade))