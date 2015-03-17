# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:01:35 2015

@author: Pedro
"""
import random

list = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']

pcp = 0
jp = 0

while pcp < 3 and jp < 3:
    pc = random.choice(list)
    jogador = str(input('Escreva sua jogada \n'))
    jogador = jogador.lower()
    print('O computador jogou ' +pc)

    if pc == 'pedra' and (jogador == 'tesoura' or jogador == 'lagarto'):
        pcp += 1
        print('Computador ganhou a rodada \n Computador ', pcp, ', Jogador ' ,jp)
    elif jogador == 'pedra' and (pc == 'tesoura' or pc == 'lagarto'):
        jp += 1
        print('Você ganhou a rodada \n Computador ', pcp ,', Jogador ' ,jp)
    elif pc == 'tesoura' and (jogador == 'papel' or jogador == 'lagarto'):
        pcp += 1
        print('Computador ganhou a rodada \n Computador ', pcp ,', Jogador ' ,jp)
    elif jogador == 'tesoura' and (pc == 'papel' or pc == 'lagarto'):
        jp += 1
        print('Você ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif pc == 'papel' and (jogador == 'pedra' or jogador == 'spock'):
        pcp += 1
        print('Computador ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif jogador == 'papel' and (pc == 'pedra' or pc == 'spock'):
        jp += 1
        print('Você ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif pc == 'lagarto' and (jogador == 'spock' or jogador == 'papel'):
        pcp += 1
        print('Computador ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif jogador == 'lagarto' and (pc == 'spock' or jogador == 'papel'):
        jp += 1
        print('Você ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif pc == 'spock' and (jogador == 'tesoura' or jogador == 'pedra'):
        pcp += 1
        print('Computador ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif jogador == 'spock' and (pc == 'tesoura' or pc == 'pedra'):
        jp += 1
        print('Você ganhou a rodada \n Computador ' ,pcp ,', Jogador ' ,jp)
    elif jogador == pc:
        print('Empate! \n Computador ', pcp ,', Jogador ' ,jp)
    else:
        print('Você digitou algo errado, procure um dicionário')

if pcp == 3:
    print('Você perceu! \n Placar final: Computador ' ,pcp ,', Jogador ' ,jp)
    
else:
    print('Você ganhou! \n Placar final: Computador ' ,pcp ,', Jogador ' ,jp)
    