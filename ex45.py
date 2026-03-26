from random import randint
jogo = str(input('Vamos jogar [sim/nao]: '))
if jogo == 'SIM' or jogo == 'sim' or jogo == 'Sim':
    print('[1] - Pedra')
    print('[2] - Papel')
    print('[3] - Tesoura')
    jogador = int(input('Escolha sua opção: '))
    if jogador == 1:
        print('Você escolheu a opção: 1 - Pedra')
    elif jogador == 2:
        print('Você escolheu a opção: 2 - Papel')
    elif jogador == 3:
        print('Você escolheu a opção: 3 - Tesoura')
    computador = randint(1,3)
    if computador == 1:
        print('O computador escolheu a opção: 1 - Pedra')
    elif computador == 2:
        print('O computador escolheu a opção: 2 - Papel')
    elif computador == 3:
        print('O computador escolheu a opção: 3 - Tesoura')
    opções = ('Pedra', 'Papel', 'Tesoura')
    if jogador == computador:
        print('Empate! Ambos escolheram {}'.format(opções[jogador - 1]))
    elif jogador == 1 and computador == 3:
        print('Você ganhou! Pedra quebra Tesoura.')
    elif jogador == 2 and computador == 1:
        print('Você ganhou! Papel embrulha Pedra.')
    elif jogador == 3 and computador == 2:
        print('Você ganhou! Tesoura corta Papel.')
    elif computador == 1 and jogador == 3:
        print('Você perdeu! Pedra quebra Tesoura.')
    elif computador == 2 and jogador == 1:
        print('Você perdeu! Papel embrulha Pedra.')
    elif computador == 3 and jogador == 2:
        print('Você perdeu! Tesoura corta Papel.')
else:
    print('Ok, fica para a proxima')
