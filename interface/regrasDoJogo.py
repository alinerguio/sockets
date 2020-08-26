# Batalha Naval - Funções que definem as Regras do Jogo
# Aline Guimarães e Alice Ribeiro
# Github: https://github.com/alinerguio/sockets

from os import system
import random
from interface import *

def criaTabuleiro():
    novoTabuleiro = []
    for _ in range(10):
        novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
    return novoTabuleiro

def colocarNavios(frame, tabuleiro):
    colocarNavio(frame, "porta aviao", 5, tabuleiro, 1)
    
    na=1
    while na <= 2:
        colocarNavio(frame, "navio tanque", 4, tabuleiro, na)
        na = na + 1

    ct = 1
    while ct <= 3:
        colocarNavio(frame, "contra torpedo", 3, tabuleiro, ct)
        ct = ct + 1

    s=1
    while s <= 4:
        colocarNavio(frame, "submarino", 2, tabuleiro, s)
        s = s + 1

def colocarNavio(frame, nome, tamanho, tabuleiro, quantidade):
    comSucesso = False
    direcaoCorreta = False

    while not comSucesso or not direcaoCorreta:
        posicao, direcao = inserir_navios(frame, nome, tamanho)
        comSucesso = validaColocarNavio(tabuleiro, posicao, tamanho)

        if(direcao == 'v' or direcao == 'h'):
            definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, tamanho)
            direcaoCorreta = True
            inserido_status(frame, "Inserido com sucesso") # muda 
        else:
            inserido_status(frame, "Tente novamente, não inserido") # muda 


def executarTiro(tabuleiro, posicao):
    linha = posicao[0]
    coluna = posicao[1]
    if tabuleiro[int(linha)][int(coluna)] == 'O':
        tabuleiro[int(linha)][int(coluna)] == 'X'
        return True
    else:
        tabuleiro[int(linha)][int(coluna)] == '.'
        return False