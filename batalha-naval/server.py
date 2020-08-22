# Batalha Naval - servidor
# Aline Guimarães e Alice Ribeiro

import socket
from regrasDoJogo import *

def server():
    host = ''
    port = 5000

    em_jogo = True
    tabuleiroproprio = []
    tabuleirooponente = []
    atingidos = 0
    jogador = '1'
    quemJoga = '1'

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    server_socket.bind((host, port))  # conecta ao servidor

    print("Aguardando conexão com cliente...")

    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceita nova conexão
    print("Conexão com: " + str(address))
    print ('Preparar, apontar....')

    tabuleiroproprio = criaTabuleiro() # cria novos tabuleiros
    tabuleirooponente = criaTabuleiro()
    imprimeRegras(jogador) # imprime as regras
    colocarNavios(tabuleiroproprio) # insere navios no tabuleiro
    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente) 

    while em_jogo:
        #---------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga

            if em_jogo:
                print("Aguarde a jogada do", address, "...")
  
                jogada = conn.recv(1024).decode() # recebe jogada do outro jogador
                
                if not jogada or jogada == '-1': # verifica se o outro jogador saiu
                    print ("Jogador desconectou")
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
                        conn.send(mensagem.encode())
                    else: # se o outro jogador errou
                        tabuleiroproprio[int(linha)][int(coluna)] = '.'
                        mensagem = '.'
                        conn.send(mensagem.encode())
                        quemJoga = '1'

                    imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)
                        
#----------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '1'): # enquanto o servidor joga
                jogada = input("\n\tJogada =>  ") # recebe jogada

                while validaJogada(tabuleirooponente, jogada) == False: # repete até jogada ser válida
                    jogada = input("Digite uma jogada válida =>  ")

        
                if not jogada or jogada == "sair" or jogada == "SAIR": # verifica se esse jogador deseja sair
                    print ('Aplicação foi finalizada\n')
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while
                    mensagem = '-1'
                    conn.send(mensagem.encode()) # envia mensagem para outro jogador que saiu 

                else: # joga

                    conn.send(jogada.encode()) # envia jogada para outro jogador
        
                    jogada_recebida = conn.recv(1024).decode() # recebe resposta sobre acerto ou erro

                    if jogada_recebida != '': 
                        linha = jogada[0]
                        coluna = jogada[1]
                        if(jogada_recebida == 'X'): # se acertou algum navio
                            tabuleirooponente[int(linha)][int(coluna)] = 'X'
                            atingidos += 1
                        else: # se errou
                            tabuleirooponente[int(linha)][int(coluna)] = '.'
                            quemJoga = '2'


                        imprimeTabuleiros(tabuleiroproprio, tabuleirooponente)

                        if atingidos == 30: # verifica se ganhou 
                            print("\nVocê Ganhou! Parabéns! :D")
                            print ("\nJogo Terminado!")
                            em_jogo = False # finaliza while
                            quemJoga = '0' # finaliza while
                            mensagem = 'fim' 
                            conn.send(mensagem.encode()) # envia mensagem ao outro jogador que ganhou
                    
    conn.close()  # fecha conexão


if __name__ == '__main__':
    server()