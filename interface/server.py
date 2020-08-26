# Batalha Naval - Servidor
# Aline Guimarães e Alice Ribeiro
# Github: https://github.com/alinerguio/sockets

from tkinter import *
import socket
from interface import *

def server(frame_t1, frame_separa, frame_t2, frame_joga):
    host = ''
    port = 5000

    em_jogo = False
    tabuleiro_proprio = []
    tabuleiro_oponente = []
    atingidos = 0
    jogador = '1'
    quemJoga = '1'

    tabuleiro_proprio = cria_tabuleiro() # cria novos tabuleiros
    tabuleiro_oponente = cria_tabuleiro()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    server_socket.bind((host, port))  # conecta ao servidor
    
    print("Aguardando conexão com cliente...")
    
    server_socket.listen(2)
    conn, address = server_socket.accept()  # aceita nova conexão

    lista_navios = navios()
    status(frame_joga, "Inserir o navio:")
    separador(frame_separa, 11, 16)
    tabuleiro(frame_t2, tabuleiro_oponente, False, 11) 
    em_jogo = insere(frame_joga, frame_t1, tabuleiro_proprio, lista_navios) # insere navios no tabuleiro

    while em_jogo:

        #---------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga

            if em_jogo:
                fim(frame_joga, "\nAguarde a jogada do ", str(address), "...")
  
                jogada = conn.recv(1024).decode() # recebe jogada do outro jogador
                
                if not jogada or jogada == '-1': # verifica se o outro jogador saiu
                    fim(frame_joga, "\nJogador desconectou")
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                elif jogada == 'fim': # verifica se o outro jogador ganhou
                    fim(frame_joga, "\nVocê Perdeu! :( \n\nJogo Terminado!")
                    em_jogo = False # finaliza while
                    quemJoga = '0' # finaliza while

                else:
                    sucesso = executarTiro(tabuleiro_proprio, jogada) # verifica a jogada do adversário

                    linha = jogada[0]
                    coluna = jogada[1]

                    if(sucesso): # se o outro jogador acertou 
                        tabuleiro_proprio[int(linha)][int(coluna)] = 'X'
                        mensagem = 'X'
                        conn.send(mensagem.encode())
                    else: # se o outro jogador errou
                        tabuleiro_proprio[int(linha)][int(coluna)] = '.'
                        mensagem = '.'
                        conn.send(mensagem.encode())
                        quemJoga = '1'

                    tabuleiro(frame_t1, tabuleiro_proprio, False, 0)
                    separador(frame_separa, 11, 13)
                    tabuleiro(frame_t2, tabuleiro_oponente, False, 11)
                        
#----------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '1'): # enquanto o servidor joga

            jogar(frame_joga, "Atacar!", frame_t2, tabuleiro_oponente)
            jogada = tabuleiro_ataque(frame_t2, tabuleiro_oponente, 11, [])

            if not jogada or jogada == "sair": # verifica se esse jogador deseja sair
                fim(frame_joga, "Aplicação foi finalizada")
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
                        tabuleiro_oponente[int(linha)][int(coluna)] = 'X'
                        atingidos += 1
                    else: # se errou
                        tabuleiro_oponente[int(linha)][int(coluna)] = '.'
                        quemJoga = '2'


                    tabuleiro(frame_t1, tabuleiro_proprio, True, 0)
                    separador(frame_separa, 11, 13)
                    tabuleiro(frame_t2, tabuleiro_oponente, False, 11)

                    if atingidos == 30: # verifica se ganhou 
                        fim(frame_joga, "\nVocê Ganhou! Parabéns! :D \n\nJogo Terminado!")
                        em_jogo = False # finaliza while
                        quemJoga = '0' # finaliza while
                        mensagem = 'fim' 
                        conn.send(mensagem.encode()) # envia mensagem ao outro jogador que ganhou

    conn.close()  # fecha conexão
    

if __name__ == '__main__':
    menu = Tk()
    frame = cria_janela(menu, "Servidor")
    server(frame[0], frame[1], frame[2], frame[3])
    menu.mainloop() 