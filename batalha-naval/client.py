# Batalha Naval - cliente
# Aline Guimarães e Alice Ribeiro

import socket
from regrasDoJogo import *

def client():
    host = '192.168.0.101'
    port = 5000

    em_jogo = True
    tabuleiroproprio = []
    tabuleirooponente = []
    atingidos = 0
    jogador = '2'
    quemJoga = '1'

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    client_socket.connect((host, port))  # conecta ao servidor

    tabuleiroproprio = criaTabuleiro() # cria novos tabuleiros
    tabuleirooponente = criaTabuleiro()
    imprimeRegras(jogador) # imprime as regras
    colocarNavios(tabuleiroproprio) # insere navios no tabuleiro
    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente) 

    print ('Preparar, apontar....')

    while em_jogo:
    #------------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga 
            jogada = input("\n\tJogada =>  ") # recebe jogada

            while validaJogada(tabuleirooponente,jogada) == False : # repete até jogada ser válida
                jogada = input("Digite uma jogada válida =>  ")

            if not jogada or jogada == "sair" or jogada == "SAIR": # verifica se esse jogador deseja sair
                print ('Aplicação foi finalizada\n')
                em_jogo = False # finaliza while
                quemJoga = '0' # finaliza while
                mensagem = '-1'
                client_socket.send(mensagem.encode()) # envia mensagem para outro jogador que saiu

            else: # joga
                client_socket.send(jogada.encode()) # envia jogada para outro jogador

                jogada_recebida = client_socket.recv(1024).decode() # recebe resposta sobre acerto ou erro

                if jogada_recebida != '':
                    linha = jogada[0]
                    coluna = jogada[1]
                    if(jogada_recebida == 'X'): # se acertou algum navio
                        tabuleirooponente[int(linha)][int(coluna)] = 'X'
                        atingidos += 1
                    else: # se errou
                        tabuleirooponente[int(linha)][int(coluna)] = '.'
                        quemJoga = '1'

                    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)
                    
                    if atingidos == 30: # verifica se ganhou 
                        print("\nVocê Ganhou! Parabéns! :D")
                        print ("\nJogo Terminado!")
                        em_jogo = False # finaliza while
                        quemJoga = '0' # finaliza while
                        mensagem = 'fim' 
                        client_socket.send(mensagem.encode()) # envia mensagem ao outro jogador que ganhou
    #---------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '1'): # enquanto o servidor joga

            if em_jogo:
                print("\nAguarde a jogada do servidor...")

                jogada = client_socket.recv(1024).decode() # recebe jogada do outro jogador

                if not jogada or jogada == '-1': # verifica se o outro jogador saiu
                    print ('\nServidor ', host, ' desconectou-se.\n')
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                elif jogada == 'fim': # verifica se o outro jogador ganhou
                    print("\nVocê Perdeu! :(")
                    print ("\nJogo Terminado!")
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                else: 
                    sucesso = executarTiro(tabuleiroproprio, jogada) # verifica a jogada do adversário

                    linha = jogada[0]
                    coluna = jogada[1]

                    if(sucesso): # se o outro jogador acertou 
                        tabuleiroproprio[int(linha)][int(coluna)] = 'X'
                        mensagem = 'X'
                        client_socket.send(mensagem.encode()) 
                    else: # se o outro jogador errou
                        tabuleiroproprio[int(linha)][int(coluna)] = '.'
                        mensagem = '.'
                        client_socket.send(mensagem.encode())
                        quemJoga = '2' 
            
                    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client()