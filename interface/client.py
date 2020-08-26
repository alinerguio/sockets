# Batalha Naval - Cliente
# Aline Guimarães e Alice Ribeiro
# Github: https://github.com/alinerguio/sockets

from tkinter import *
import socket
from interface import *

def client(frame_t1, frame_separa, frame_t2, frame_joga):
    host = '192.168.0.101' # ip da rede a ser conectada - deve ser mudado de acordo com o ip de conexão do servidor
    port = 5000

    em_jogo = False
    atingidos = 0
    tabuleiro_proprio = []
    tabuleiro_oponente = []
    quemJoga = '1'

    tabuleiro_proprio = cria_tabuleiro() # cria novos tabuleiros
    tabuleiro_oponente = cria_tabuleiro()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    client_socket.connect((host, port))  # conecta ao servidor

    lista_navios = navios()

    status(frame_joga, "Inserir o navio:")
    separador(frame_separa, 11, 16)
    tabuleiro(frame_t2, tabuleiro_oponente, False, 11)
    em_jogo = insere(frame_joga, frame_t1, tabuleiro_proprio, lista_navios) # insere navios no tabuleiro
    separador(frame_separa, 11, 16)
    tabuleiro(frame_t2, tabuleiro_oponente, False, 11)  

    while em_jogo:
    #------------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga 
            jogar(frame_joga, "Atacar!", frame_t2, tabuleiro_oponente)
            jogada = tabuleiro_ataque(frame_t2, tabuleiro_oponente, 11, [])

            if not jogada or jogada == "sair": # verifica se esse jogador deseja sair
                fim(frame_joga, "Aplicação foi finalizada")
                em_jogo = False # finaliza while
                quemJoga = '0' # finaliza while
                mensagem = '-1'
                client_socket.send(mensagem.encode()) # envia mensagem para outro jogador que saiu

            else: # joga
                client_socket.send(jogada.encode()) # envia jogada para outro jogador

                jogada_recebida = client_socket.recv(1024).decode() # recebe resposta sobre acerto ou erro

                acertei = False
                if jogada_recebida != '':
                    linha = jogada[0]
                    coluna = jogada[1]
                    if(jogada_recebida == 'X'): # se acertou algum navio
                        tabuleiro_oponente[int(linha)][int(coluna)] = 'X'
                        atingidos += 1
                        acertei = True
                    else: # se errou
                        tabuleiro_oponente[int(linha)][int(coluna)] = '.'
                        quemJoga = '1'
                        acertei = False

                    tabuleiro(frame_t1, tabuleiro_proprio, False, 0)
                    separador(frame_separa, 11, 13)
                    tabuleiro(frame_t2, tabuleiro_oponente, acertei, 11)
                    
                    if atingidos == 30: # verifica se ganhou 
                        fim(frame_joga, "\nVocê Ganhou! Parabéns! :D \n\nJogo Terminado!")
                        em_jogo = False # finaliza while
                        quemJoga = '0' # finaliza while
                        mensagem = 'fim' 
                        client_socket.send(mensagem.encode()) # envia mensagem ao outro jogador que ganhou
    #---------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '1'): # enquanto o servidor joga

            if em_jogo:
                tabuleiro(frame_t1, tabuleiro_proprio, False, 0)
                separador(frame_separa, 11, 13)
                tabuleiro(frame_t2, tabuleiro_oponente, False, 11)

                fim(frame_joga, "\nAguarde a jogada do servidor...")

                jogada = client_socket.recv(1024).decode() # recebe jogada do outro jogador

                if not jogada or jogada == '-1': # verifica se o outro jogador saiu
                    fim(frame_joga, "\nServidor " + str(host) + " desconectou-se.\n")
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                elif jogada == 'fim': # verifica se o outro jogador ganhou
                    fim(frame_joga, "\nVocê Perdeu! :( \n\nJogo Terminado!")
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                else: 
                    sucesso = executar_tiro(tabuleiro_proprio, jogada) # verifica a jogada do adversário

                    linha = jogada[0]
                    coluna = jogada[1]

                    errou = False
                    if(sucesso): # se o outro jogador acertou 
                        tabuleiro_proprio[int(linha)][int(coluna)] = 'X'
                        mensagem = 'X'
                        errou = False
                        client_socket.send(mensagem.encode()) 
                    else: # se o outro jogador errou
                        tabuleiro_proprio[int(linha)][int(coluna)] = '.'
                        mensagem = '.'
                        errou = True
                        client_socket.send(mensagem.encode())
                        quemJoga = '2' 
            
                    tabuleiro(frame_t1, tabuleiro_proprio, False, 0)
                    separador(frame_separa, 11, 13)
                    tabuleiro(frame_t2, tabuleiro_oponente, errou, 11)

    client_socket.close()  # close the connection
    menu.mainloop()

if __name__ == '__main__':
    menu = Tk()
    frame = cria_janela(menu, "Cliente")
    client(frame[0], frame[1], frame[2], frame[3])
    menu.mainloop() 