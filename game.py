from sys import exit
from random import randint

idioma = int(input('ESCOLHA/SELECT \n [1] Portuguese \n [2] English \n ~>'))
escolha0 = randint(1,3)
escolha1 = []
if idioma == 1:
    if escolha0 == 1:
        escolha1 = int(input('Escolha uma das opções abaixo \n [1] Pedra \n [2] Papel \n [3] Tesoura \n ~>'))
        if escolha1 == 1:
            print('O computador escolheu Pedra \n O jogador escolheu Pedra \n EMPATE')
        elif escolha1 == 2:
            print('O computador escolheu Pedra \n O jogador escolheu Papel \n JOGADOR VENCEU!')
        elif escolha1 == 3:
            print('O computador escolheu Pedra \n O jogador escolheu Tesoura \n COMPUTADOR VENCEU!')
        else:
            print('Escolha invalída')
    elif escolha0 == 2:
        escolha1 = int(input('Escolha uma das opções abaixo \n [1] Pedra \n [2] Papel \n [3] Tesoura \n ~>'))
        if escolha1 == 1:
            print('O computador escolheu Papel \n O jogador escolheu Pedra \n COMPUTADOR VENCEU!')
        elif escolha1 == 2:
            print('O computador escolheu Papel \n O jogador escolheu Papel \n EMPATE')
        elif escolha1 == 3:
            print('O computador escolheu Papel \n O jogador escolheu Tesoura \n JOGADOR VENCEU!')
        else:
            print('Escolha invalída')
    elif escolha0 == 3:
        escolha1 =int(input('Escolha uma das opções abaixo \n [1] Pedra \n [2] Papel \n [3] Tesoura \n ~>'))
        if escolha1 == 1:
            print('O computador escolheu Tesoura \n O jogador escolheu Pedra \n JOGADOR VENCEU!') 
        elif escolha1 == 2:
            print('O computador escolheu Tesoura \n O jogador escolheu Papel \n COMPUTADOR VENCEU!')
        elif escolha1 == 3:
            print('O computador escolheu Tesoura \n O jogador escolheu Tesoura \n EMPATE')
        else:
            print('Escolha invalída')
    else:
        print('Erro de escolha do computador')
elif idioma == 2:
    if escolha0 == 1:
        escolha1 = int(input('Choice the options below \n [1] Stone \n [2] Paper \n [3] Scissors \n ~>'))
        if escolha1 == 1:
            print('The computer choice Stone \n The player choice Stone \n Draw')
        elif escolha1 == 2:
            print('The computer choice Stone \n The player choice Paper  \n PLAYER WINS!')
        elif escolha1 == 3:
            print('The computer choice Stone \n The player choice Scissors \n COMPUTER WINS!')
        else:
            print('Choice incorrect')
    elif escolha0 == 2:
        escolha1 = int(input('Choice the options below \n [1] Stone \n [2] Paper \n [3] Scissors \n ~>'))
        if escolha1 == 1:
            print('The computer choice Paper \n The player choice Stone \n COMPUTER WINS!')
        elif escolha1 == 2:
            print('The computer choice Paper \n The player choice Paper \n Draw')
        elif escolha1 == 3:
            print('The computer choice Paper \n The player choice Scissors \n PLAYERS WINS!')
        else:
            print('Choice incorrect')
    elif escolha0 == 3:
        escolha1 =int(input('Choice the options below \n [1] Stone \n [2] Paper \n [3] Scissors \n ~>'))
        if escolha1 == 1:
            print('The computer choice Scissors \n The player choice Stone \n PLAYER WINS!') 
        elif escolha1 == 2:
            print('The computer choice Scissors \n The player choice Paper \n COMPUTER WINS!')
        elif escolha1 == 3:
            print('The computer choice Scissors \n The player choice Scissors \n Draw')
        else:
            print('Choice incorrect')
    else:
        print('Erro of computer')
else:
    print('Opção invalída/ Option incorrect')
    exit('') 