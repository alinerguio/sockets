# Batalha Naval - cliente
# Aline Guimarães e Alice Ribeiro
# Repositório github: https://github.com/alinerguio/sockets

import socket
from regrasDoJogo import *

def client():
    # ip da rede a ser conectada - deve ser mudado de acordo com o ip de conexão do servidor
    host = '192.168.0.101' 
    port = 5000 # porta a ser utilizada

    # variavel que controla se um jogo está em andamento e seu encerramento
    em_jogo = True
    tabuleiroproprio = [] # tabuleiro do usuario cliente
    # tabuleiro do oponente(servidor), somente com as ações e jogadas ja executadas
    tabuleirooponente = []
    atingidos = 0 # contador que monitora o fim do jogo, se e quem ganhou
    jogador = '2' # id do jogador
    quemJoga = '1' # define de quem e a vez, sempre começa com o 1, pois ele foi o que primeiro conectou

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    client_socket.connect((host, port))  # conecta ao servidor

    # cria novos tabuleiros
    # o do usuário sera preenchido mais tarde e o do oponente ficará anonimo
    tabuleiroproprio = criaTabuleiro() # cria novos tabuleiros
    tabuleirooponente = criaTabuleiro()
    imprimeRegras(jogador) # imprime as regras
    colocarNavios(tabuleiroproprio) # insere navios no tabuleiro
    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente) # imprime os dois tabuleiros lado a lado

    print ('Preparar, apontar....')

    while em_jogo:
    #------------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga 
            jogada = input("\n\tJogada =>  ") # recebe jogada

            while validaJogada(tabuleirooponente,jogada) == False : # repete até jogada ser válida
                jogada = input("Digite uma jogada válida =>  ")

            if not jogada or jogada == "sair" or jogada == "SAIR": # verifica se esse jogador deseja sair
                print ('Aplicação foi finalizada\n')
                em_jogo = False # finaliza while externo
                quemJoga = '0' # finaliza while interno
                mensagem = '-1'
                client_socket.send(mensagem.encode()) # envia mensagem para outro jogador avisando que o cliente saiu

            else: # a jogada e uma posicao LC, a vez do cliente executar a jogada
                # envia jogada para outro jogador, para que ele veja o que tem no tabuleiro na posicao indicada
                client_socket.send(jogada.encode()) 

                # recebe o resultado da jogada
                #'X' significa que acretou algo e '.' que estava vazio
                jogada_recebida = client_socket.recv(1024).decode() # recebe resposta sobre acerto ou erro

                if jogada_recebida != '': # se a resposta nao for vazia
                    # separa linha e coluna
                    linha = jogada[0]
                    coluna = jogada[1]
                    if(jogada_recebida == 'X'): # se acertou algum navio
                        tabuleirooponente[int(linha)][int(coluna)] = 'X'
                        atingidos += 1 #contador pra quantas celulas foram atingidas
                    else: # se errou
                        tabuleirooponente[int(linha)][int(coluna)] = '.'
                        quemJoga = '1' #muda de jogador somente quando erra

                    #imprime os tabuleiros atualizados
                    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)
                    
                    if atingidos == 30: # verifica se ganhou 
                        print("\nUHUUUUUL! Parabéns! :D")
                        print ("\nJogo Terminado!")
                        em_jogo = False # finaliza while externo
                        quemJoga = '0' # finaliza while interno
                        # mensagem pra indicar para o outro jogador que quem enviou ganhou
                        mensagem = 'fim' 
                        client_socket.send(mensagem.encode()) # envia mensagem ao outro jogador para avisar que ele perdeu
    #---------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '1'): # enquanto o servidor joga

            if em_jogo: #esperando a jogada do servidor
                print("\nAguarde a jogada do servidor...")

                jogada = client_socket.recv(1024).decode() # recebe jogada do outro jogador

                if not jogada or jogada == '-1': # verifica se o outro jogador saiu
                    print ('\nServidor ', host, ' desconectou-se.\n')
                    em_jogo = False # finaliza while externo
                    quemJoga = '0' # finaliza while interno

                elif jogada == 'fim': # verifica se o outro jogador ganhou
                    print("\nVocê Perdeu! :(")
                    print ("\nJogo Terminado!")
                    em_jogo = False # finaliza while externo
                    quemJoga = '0' # finaliza while interno

                else: 
                    # verifica o resultado da jogada do adversário contra o usuário
                    sucesso = executarTiro(tabuleiroproprio, jogada) # verifica a jogada do adversário

                    #separa a resposta em linha e coluna
                    linha = jogada[0]
                    coluna = jogada[1]

                    #'X' significa que acretou algo e '.' que a posicao estava vazio
                    if(sucesso): # se o outro jogador acertou 
                        tabuleiroproprio[int(linha)][int(coluna)] = 'X' #atualiza seu tabuleiro
                        mensagem = 'X'
                        client_socket.send(mensagem.encode()) 
                        #continua a jogar ate que acerte um campo vazio
                    else: # se o outro jogador errou
                        tabuleiroproprio[int(linha)][int(coluna)] = '.'
                        mensagem = '.'
                        client_socket.send(mensagem.encode())
                        quemJoga = '2' #passa a vez pro adversario
            
                    #imprime ambas as malhas apos as acoes
                    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client()