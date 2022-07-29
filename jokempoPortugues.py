from random import randint
from sys import exit

print('         Bem vindo\n     Jokempô terminal')
escolha_jogador = int(input('Escolha uma das opções \n [1] Pedra \n [2] Papel \n [3] Tesoura \n [4] Sair\n ~>'))
escolha_pc = randint(1,3)
if escolha_pc == 1:
    if escolha_jogador == 1:
        print('O computador escolheu Pedra\n O jogador escolheu Pedra \nresultado:\nEmpate')
    elif escolha_jogador == 2:
        print('O computador escolheu Pedra\n O jogador escolheu Papel \nresultado:\nJogador ganhou')
    elif escolha_jogador == 3:
        print('O computador escolheu Pedra\n O jogador escolheu Tesoura \nresultado:\nComputador ganhou')
    else:
        print('Até mais')
if escolha_pc == 2:
    if escolha_jogador == 1:
        print('O computador escolheu Papel\n O jogador escolheu Pedra \nresultado:\nComputador ganhou')
    elif escolha_jogador == 2:
        print('O computador escolheu Papel\n O jogador escolheu Papepl \nresultado:\nEmpate')
    elif escolha_jogador == 3:
        print('O computador escolheu Papel\n O jogador escolheu Tesoura \nresultado:\njogador ganhou')
    else:
        print('Até mais')
if escolha_pc == 3:
    if escolha_jogador == 1:
        print('O computador escolheu Tesoura\n O jogador escolheu Pedra \nresultado:\nJogador ganhou')
    elif escolha_jogador == 2:
        print('O computador escolheu Tesoura\n O jogador escolheu Papel \nresultado:\nComputador ganhou')
    elif escolha_jogador == 3:
        print('O computador escolheu Tesoura\n O jogador escolheu Tesoura \nresultado: \nEmpate')
    else:
        print('Até mais')




