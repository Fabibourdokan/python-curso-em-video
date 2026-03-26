from datetime import date
ano_atual = date.today().year
ano = input('Ano de nascimento: ')
idade = ano_atual - int(ano)
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, ano_atual))
if idade < 18:
    print('Ainda não está na hora de se alistar! Faltam {} anos.'.format(18 - idade))
elif idade == 18:
    print('Já esta na hora de se alistar!')
else:
    print('Já se passaram {} anos do seu alistamento.'.format(idade - 18))
