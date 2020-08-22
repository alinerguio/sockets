from os import system
import random

# definir todos os navios do jogador, feito no começo do jogo
# Sao 1 porta aviao, 2 navios tanques, 3 contra torpedos, 4 submarinos
# cada um com seu tamanho especifico
# dividido em mais funcoes para ser mais facil de entender e de debugar
def colocarNavios(tabuleiro):
    print("Defina seus navios no tabuleiro")

    # chama uma funcao para verificar as entradas e definir onde navio ira ficar
    # só tem 1 porta aviao
    colocarNavio("porta aviao", 5, tabuleiro, 1)
    
    # chama uma funcao para verificar as entradas e definir onde navio ira ficar
    # tem um while pra colocar os 2 navios tanques e colocam qual o navio esta pra deixar claro para o usuário
    na=1
    while na <= 2:
        colocarNavio("navio tanque", 4, tabuleiro, na)
        na = na + 1

    # chama uma funcao para verificar as entradas e definir onde navio ira ficar
    # tem um while pra colocar os 3 contra torpedo e colocam qual o navio esta pra deixar claro para o usuário
    ct = 1
    while ct <= 3:
        colocarNavio("contra torpedo", 3, tabuleiro, ct)
        ct = ct + 1

    # chama uma funcao para verificar as entradas e definir onde navio ira ficar
    # tem um while pra colocar os 4 submarino e colocam qual o navio esta pra deixar claro para o usuário
    s=1
    while s <= 4:
        colocarNavio("submarino", 2, tabuleiro, s)
        s = s + 1

#verfifica a se posicao do navio é valida, se a direção do navio é valida e se o navio cabe na malha
def colocarNavio(nome, tamanho, tabuleiro, quantidade):
    # imprime algumas indicações pro usuário: posicao da entrada, nome e qual navio esta sendo utilizada
    posicao= input("Insira a posição do navio (linhaxcoluna) "+ nome + " " + str(quantidade)+": ")
    #verifica se a posicao inserida é valida
    comSucesso = validaJogada(tabuleiro, posicao)
    while not comSucesso: # repete enquanto a posicao é invalida
        posicao= input("Insira a posição do navio (linhaxcoluna): ")
        comSucesso = validaJogada(tabuleiro, posicao)

    direcaoCorreta = False
    while not direcaoCorreta: # enquanto a direcao nao é valida repete
        #informa o usuário que a direção deve ser v(vertical) ou h(horizontal)
        direcao = input("Insira a direção do navio(v/h): ")
        # verifica se é v ou h
        if( direcao == 'v' or direcao == 'h'):
            # coloca o navio se cabe na malha
            cabeNaMalha = False
            while not cabeNaMalha:
                cabeNaMalha = definirNavios(tabuleiro, int(posicao[0]), int(posicao[1]), direcao, tamanho)
            direcaoCorreta = True # encerra o while
        else:
            print("A direção dever ser v(vertical) ou h(horizontal)")

# colocar o navio, se cabe na malha
def definirNavios(tabuleiro, linha, coluna, direcao, tamanho):
    if direcao == 'h': # se o navio for posicionado na horizontal
        # se o tamanho do navio, mas a coluna que ele vai comecar a ser posicionado, é menor que o tamanho da malha
        if(tamanho+coluna > 10): 
            print("Navio não cabe na malha.Tente novamente")
            return False
        else: # se cabe
            while tamanho > 0: # enquanto o tamanho é maior que zero
                tabuleiro[linha][coluna] = 'O' # adiciona uma 'parte' do navio
                tamanho = tamanho - 1 # diminui o tamanho para continuar a colocar
                coluna = coluna + 1 #aumenta a coluna para do lado, enquanto o tamanho for maior que zero, a linha permanece a mensma
    else: # se o navio for posicionado na vertical
        # se o tamanho do navio, mas a linha que ele vai comecar a ser posicionado, é menor que o tamanho da malha
        if(tamanho+linha > 10): 
            print("Navio não cabe na malha.Tente novamente")
            return False
        else: # se cabe
            while tamanho > 0: # enquanto o tamanho é maior que zero
                tabuleiro[linha][coluna] = 'O' # adiciona uma 'parte' do navio
                tamanho = tamanho - 1 # diminui o tamanho para continuar a colocar
                linha = linha + 1 #aumenta a linha para do baixo, enquanto o tamanho for maior que zero, a coluna permanece a mensma
    return True # se checar até aqui é porque cabe

#imprime as regras para o jogador
def imprimeRegras(jogador):    
    print("##------------------------------------------------------------##")
    print("##------------------------ BATALHA NAVAL ---------------------##")
    print("##------------------------------------------------------------##")
    print("##                          ~INSTRUÇÕES~                      ##")
    print("## Você é o jogador ", jogador, ". Para sair do jogo, digite 'sair'    ##")
    return

# imprime um tabuleiro do lado do outro, por questões de usabilidade
# star wars reference ;)
def imprimeTabuleiros(tabuleiro1, tabuleiro2):
    
    print("              Defenda |o|                                      Ataque |o|")
    print("   0   1   2   3   4   5   6   7   8   9              0   1   2   3   4   5   6   7   8   9")
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

# cria o tabuleiro (10x10) vazio
def criaTabuleiro():
	novoTabuleiro = []
	for _ in range(10):
		novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
	return novoTabuleiro

# valida a jogada
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

# executa o tiro e ver se acerta algo ou nao
def executarTiro(tabuleiro, posicao):
    linha = posicao[0]
    coluna = posicao[1]
    if tabuleiro[int(linha)][int(coluna)] == 'O':
        tabuleiro[int(linha)][int(coluna)] == 'X'
        return True
    else:
        tabuleiro[int(linha)][int(coluna)] == '.'
        return False