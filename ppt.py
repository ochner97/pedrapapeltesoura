#!/usr/bin/env python
# coding: utf-8

# PEDRA, PAPEL, TESOURA - TODO CÓDIGO GERADO POR OCHNER97 -- USO DE IA APENAS PARA ORIENTAÇÃO DE CONCEITOS.
# CIENTE DA IMPORTÂNCIA DA IA PARA PROJETOS, MAS POR ESTAR NO PROCESSO DE APRENDIZADO DE PROGRAMAÇÃO, ESCREVO CÓDIGO DESSA FORMA.


import random

def main():
    print('''Jogo do Pedra, Papel, Tesoura
    Digite 'Pedra, Papel ou Tesoura' e jogue contra o PC!''')

    while True:
        jogada_user = input('') #Jogada do usuário
        duelo(jogada_user)

def duelo(jogada_user):
    if jogada_user == 'pedra':
        jogadas = {'pedra': 0, 'papel': 1, 'tesoura': -1}
    elif jogada_user == 'papel':
        jogadas = {'pedra': -1, 'papel': 0, 'tesoura': 1}
    elif jogada_user == 'tesoura':
        jogadas = {'pedra': 1, 'papel': -1, 'tesoura': 0}

    jogada_pc = random.choice(list(jogadas.keys()))

    if jogadas[jogada_user] > jogadas[jogada_pc]:
        print(f'Você jogou {jogada_user.upper()}\nO PC jogou {jogada_pc.upper()}')
        print('Você venceu!')
    elif jogada_user == jogada_pc:
        print(f'Você jogou {jogada_user.upper()}\nO PC jogou {jogada_pc.upper()}')
        print('Empate!')
    else:
        print(f'Você jogou {jogada_user.upper()}\nO PC jogou {jogada_pc.upper()}')
        print('Você perdeu!')
# In[ ]:




