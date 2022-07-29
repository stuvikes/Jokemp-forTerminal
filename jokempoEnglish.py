# jokempo
from sys import exit
import random


print('Welcome to jokempo for terminal \n', '-=' * 10)
escolha1 = random.randint(1,3)
escolha2 = int(input('Choice one the of the options\n 1- Rock\n 2- Paper\n 3- Scissors\n <-->'))
if type(escolha2) == [str, bool, float]:
    print('Your choice is invalid')
    exit('')

if escolha1 == 1:
    if escolha2 == 1:
        print('The computer choice ROCK and you too choice ROCK, the result is: \n<you DRAW>')
    elif escolha2 == 2:
        print('The computer choice Rock and you choice Paper, the result is: \n<you WIN>')
    elif escolha2 == 3:
        print('The computer choice Rock and you choice Scissors, the result is: \n<you DEFEAT>')
    else:
        print('The choice of the player is incorrect!')

if escolha1 == 2:
    if escolha2 == 1:
        print('The computer choice PAPER and you choice ROCK, the result is: \n<you DEFEAT>')
    elif escolha2 == 2:
        print('The computer choice PAPER and you too choice PAPER, the result is: \n<you DRAW>')
    elif escolha2 == 3:
        print('The computer choice PAPER and you choice SCISSORS, the result is: \n<you WIN>')
    else:
        print('The choice of the player is incorrect!')

if escolha1 == 3:
    if escolha2 == 1:
        print('The computer choice SCISSORS and you choice ROCK, the result is: \n<you WIN>')
    elif escolha2 == 2:
        print('The computer choice SCISSORS and you PAPER, the result is: \n<you DEFEAT>')
    elif escolha2 ==3:
        print('The computer choice SCISSORS and you too choice SCISSORS: \n<you DRAW>')
    else:
        print('The choice of the player is incorrect!')

