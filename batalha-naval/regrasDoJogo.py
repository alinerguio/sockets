from os import system
import random

def colocarNavios(tabuleiro):
    print("Defina seus navios no tabuleiro")

    colocarNavio("porta aviao", 5, tabuleiro, 1)
    
    na=1
    while na <= 2:
        colocarNavio("navio tanque", 4, tabuleiro, na)
        na = na + 1

    ct = 1
    while ct <= 3:
        colocarNavio("contra torpedo", 3, tabuleiro, ct)
        ct = ct + 1

    s=1
    while s <= 4:
        colocarNavio("submarino", 2, tabuleiro, s)
        s = s + 1

def colocarNavio(nome, tamanho, tabuleiro, quantidade):
    posicao= input("Insira a posição do navio (linhaxcolunaxposicao) "+ nome + " " + str(quantidade)+": ")
    comSucesso = validaColocarNavio(tabuleiro, posicao, tamanho)
    while not comSucesso:
        posicao= input("Insira a posição do navio(LC): ")
        comSucesso = validaColocarNavio(tabuleiro, posicao, tamanho)
    direcaoCorreta = False
    while not direcaoCorreta:
        direcao = input("Insira a direção do navio(v/h): ")
        if( direcao == 'v' or direcao == 'h'):
            definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, tamanho)
            direcaoCorreta = True
        else:
            print("A direção dever ser v(vertical) ou h(horizontal)")

def definirNavios(tabuleiro, linha, coluna, direcao, tamanho):
    if direcao == 'h':
        if(tamanho+coluna > 10): 
            print("Navio não cabe na malha.Tente novamente")
        else:
            while tamanho > 0:
                tabuleiro[linha][coluna] = 'O'
                tamanho = tamanho - 1
                coluna = coluna + 1
    else:
        if(tamanho+linha > 10): 
            print("Navio não cabe na malha.Tente novamente")
        else:
            while tamanho > 0:
                tabuleiro[linha][coluna] = 'O'
                tamanho = tamanho - 1
                linha = linha + 1

def imprimeRegras(jogador):    
    print("##------------------------------------------------------------##")
    print("##------------------------ BATALHA NAVAL ---------------------##")
    print("##------------------------------------------------------------##")
    print("##                          ~INSTRUÇÕES~                      ##")
    print("## Você é o jogador ", jogador, ". Para sair do jogo, digite 'sair'    ##")
    return

def imprimeTabuleiros(tabuleiro1, tabuleiro2):
    
    print("              Defenda |o|                                      Ataque |o|")
    print("  0   1   2   3   4   5   6   7   8   9            0   1   2   3   4   5   6   7   8   9")
    print("  ______________________________________             ______________________________________")
    print("0| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           0| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
        % ( tabuleiro1[0][0], tabuleiro1[0][1], tabuleiro1[0][2], tabuleiro1[0][3], tabuleiro1[0][4], tabuleiro1[0][5], tabuleiro1[0][6], tabuleiro1[0][7], tabuleiro1[0][8],tabuleiro1[0][9],
        tabuleiro2[0][0], tabuleiro2[0][1], tabuleiro2[0][2], tabuleiro2[0][3], tabuleiro2[0][4], tabuleiro2[0][5], tabuleiro2[0][6], tabuleiro2[0][7], tabuleiro2[0][8],tabuleiro2[0][9]) )
    print("  --------------------------------------             ---------------------------------------")
    print("1| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           1| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
        % ( tabuleiro1[1][0], tabuleiro1[1][1], tabuleiro1[1][2], tabuleiro1[1][3], tabuleiro1[1][4], tabuleiro1[1][5], tabuleiro1[1][6], tabuleiro1[1][7], tabuleiro1[1][8],tabuleiro1[1][9],
        tabuleiro2[1][0], tabuleiro2[1][1], tabuleiro2[1][2], tabuleiro2[1][3], tabuleiro2[1][4], tabuleiro2[1][5], tabuleiro2[1][6], tabuleiro2[1][7], tabuleiro2[1][8],tabuleiro2[1][9]) )
    print("  ---------------------------------------            ---------------------------------------")
    print("2| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           2| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
        % ( tabuleiro1[2][0], tabuleiro1[2][1], tabuleiro1[2][2], tabuleiro1[2][3], tabuleiro1[2][4], tabuleiro1[2][5], tabuleiro1[2][6], tabuleiro1[2][7], tabuleiro1[2][8],tabuleiro1[2][9],
        tabuleiro2[2][0], tabuleiro2[2][1], tabuleiro2[2][2], tabuleiro2[2][3], tabuleiro2[2][4], tabuleiro2[2][5], tabuleiro2[2][6], tabuleiro2[2][7], tabuleiro2[2][8],tabuleiro2[2][9]) )
    print(" ---------------------------------------             ----------------------------------------")
    print("3| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           3| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
            % ( tabuleiro1[3][0], tabuleiro1[3][1], tabuleiro1[3][2], tabuleiro1[3][3], tabuleiro1[3][4], tabuleiro1[3][5], tabuleiro1[3][6], tabuleiro1[3][7], tabuleiro1[3][8],tabuleiro1[3][9],
            tabuleiro2[3][0], tabuleiro2[3][1], tabuleiro2[3][2], tabuleiro2[3][3], tabuleiro2[3][4], tabuleiro2[3][5], tabuleiro2[3][6], tabuleiro2[3][7], tabuleiro2[3][8],tabuleiro2[3][9]) )
    print(" ---------------------------------------             ---------------------------------------")
    print("4| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           4| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
            % ( tabuleiro1[4][0], tabuleiro1[4][1], tabuleiro1[4][2], tabuleiro1[4][3], tabuleiro1[4][4], tabuleiro1[4][5], tabuleiro1[4][6], tabuleiro1[4][7], tabuleiro1[4][8],tabuleiro1[4][9],
            tabuleiro2[4][0], tabuleiro2[4][1], tabuleiro2[4][2], tabuleiro2[4][3], tabuleiro2[4][4], tabuleiro2[4][5], tabuleiro2[4][6], tabuleiro2[4][7], tabuleiro2[4][8],tabuleiro2[4][9]) )
    print(" ---------------------------------------             ---------------------------------------")
    print("5| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           5| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c " 
            % ( tabuleiro1[5][0], tabuleiro1[5][1], tabuleiro1[5][2], tabuleiro1[5][3], tabuleiro1[5][4], tabuleiro1[5][5], tabuleiro1[5][6], tabuleiro1[5][7], tabuleiro1[5][8],tabuleiro1[5][9],
            tabuleiro2[5][0], tabuleiro2[5][1], tabuleiro2[5][2], tabuleiro2[5][3], tabuleiro2[5][4], tabuleiro2[5][5], tabuleiro2[5][6], tabuleiro2[5][7], tabuleiro2[5][8],tabuleiro2[5][9]) )
    print("  ---------------------------------------            ---------------------------------------")
    print("6| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           6| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
           % ( tabuleiro1[6][0], tabuleiro1[6][1], tabuleiro1[6][2], tabuleiro1[6][3], tabuleiro1[6][4], tabuleiro1[6][5], tabuleiro1[6][6], tabuleiro1[6][7], tabuleiro1[6][8],tabuleiro1[6][9],
           tabuleiro2[6][0], tabuleiro2[6][1], tabuleiro2[6][2], tabuleiro2[6][3], tabuleiro2[6][4], tabuleiro2[6][5], tabuleiro2[6][6], tabuleiro2[6][7], tabuleiro2[6][8],tabuleiro2[6][9]) )
    print("  ---------------------------------------            ---------------------------------------")
    print("7| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           7| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
           % ( tabuleiro1[7][0], tabuleiro1[7][1], tabuleiro1[7][2], tabuleiro1[7][3], tabuleiro1[7][4], tabuleiro1[7][5], tabuleiro1[7][6], tabuleiro1[7][7], tabuleiro1[7][8],tabuleiro1[7][9],
           tabuleiro2[7][0], tabuleiro2[7][1], tabuleiro2[7][2], tabuleiro2[7][3], tabuleiro2[7][4], tabuleiro2[7][5], tabuleiro2[7][6], tabuleiro2[7][7], tabuleiro2[7][8],tabuleiro2[7][9]) )
    print("  ---------------------------------------            ---------------------------------------")
    print("8| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           8| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
            % ( tabuleiro1[8][0], tabuleiro1[8][1], tabuleiro1[8][2], tabuleiro1[8][3], tabuleiro1[8][4], tabuleiro1[8][5], tabuleiro1[8][6], tabuleiro1[8][7], tabuleiro1[8][8],tabuleiro1[8][9],
            tabuleiro2[8][0], tabuleiro2[8][1], tabuleiro2[8][2], tabuleiro2[8][3], tabuleiro2[8][4], tabuleiro2[8][5], tabuleiro2[8][6], tabuleiro2[8][7], tabuleiro2[8][8],tabuleiro2[8][9]) )
    print("  ---------------------------------------            ---------------------------------------")
    print("9| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c           9| %c | %c | %c | %c | %c | %c | %c | %c | %c | %c" 
            % ( tabuleiro1[9][0], tabuleiro1[9][1], tabuleiro1[9][2], tabuleiro1[9][3], tabuleiro1[9][4], tabuleiro1[9][5], tabuleiro1[9][6], tabuleiro1[9][7], tabuleiro1[9][8],tabuleiro1[9][9],
            tabuleiro2[9][0], tabuleiro2[9][1], tabuleiro2[9][2], tabuleiro2[9][3], tabuleiro2[9][4], tabuleiro2[9][5], tabuleiro2[9][6], tabuleiro2[9][7], tabuleiro2[9][8],tabuleiro2[9][9]) )
    print("  ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻            ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
    return

def criaTabuleiro():
	novoTabuleiro = []
	for _ in range(10):
		novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
	return novoTabuleiro


def validaColocarNavio(tabuleiro, jogada, tamanho) :
    if jogada == "sair" : 
        return True
    if len(jogada) != 2 :
        print("\tO formato correto é LC!") 
        return False
    if tabuleiro[int(jogada[0])][int(jogada[1])] != '-':
        print("\tEssa jogada já foi feita. Tente novamente") 
        return False
    if int(jogada[0]) >10 or int(jogada[1]) >10:
        print("\tO navio não cabe no tabuleiro. Tente novamente") 
        return False
    return True

def validaJogada(tabuleiro, jogada) :
    if jogada == "sair" : 
        return True
    if len(jogada) != 2 :
        print("\tO formato correto é LC!") 
        return False
    if tabuleiro[int(jogada[0])][int(jogada[1])] != '-':
        print("\tEssa jogada já foi feita. Tente novamente") 
        return False
    return True

def executarTiro(tabuleiro, posicao):
    linha = posicao[0]
    coluna = posicao[1]
    if tabuleiro[int(linha)][int(coluna)] == 'O':
        tabuleiro[int(linha)][int(coluna)] == 'X'
        return True
    else:
        tabuleiro[int(linha)][int(coluna)] == '.'
        return False