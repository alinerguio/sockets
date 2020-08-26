# Batalha Naval - Cliente
# Aline Guimarães e Alice Ribeiro
# Github: https://github.com/alinerguio/sockets

from tkinter import *
import socket
from regrasDoJogo import *
from interface import *

def client():
    host = '192.168.0.101' # ip da rede a ser conectada - deve ser mudado de acordo com o ip de conexão do servidor
    port = 5000

    em_jogo = True
    atingidos = 0
    tabuleiro_proprio = []
    tabuleiro_oponente = []
    quemJoga = '1'

    tabuleiro_proprio = criaTabuleiro() # cria novos tabuleiros
    tabuleiro_oponente = criaTabuleiro()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instancia o socket tcp
    client_socket.connect((host, port))  # conecta ao servidor

    # criação da janela e seus frames 
    menu = Tk()
    menu.title("Batalha Naval")
    menu.geometry("870x500")

    frame_labels = Frame(menu)
    frame_labels.grid(sticky=N)

    frame_meio = Frame(menu)
    frame_meio.grid()

    frame_t1 = Frame(frame_meio)
    frame_t1.grid(row=0, column=5)
    frame_separa = Frame(frame_meio)
    frame_separa.grid(row=0, column=16)
    frame_t2 = Frame(frame_meio)
    frame_t2.grid(row=0, column=18)

    frame_joga = Frame(menu)
    frame_joga.grid(rowspan=5, sticky=SW, pady=20, padx=5)

    # impressão das informações 

    w = Label(frame_labels, text="Meu Jogo", font=("Courier", 20))
    w.grid(row=0, column=5, padx=150, pady=10)
    w = Label(frame_labels, text="Jogo Rival", font=("Courier", 20))
    w.grid(row=0, column=20, padx=150, pady=10)

    tabuleiro(frame_t1, tabuleiro_proprio, True, 0)
    separador(frame_separa, 11, 13)
    tabuleiro(frame_t2, tabuleiro_oponente, False, 11)

    colocarNavios(frame_joga, tabuleiro_proprio) # insere navios no tabuleiro

    while em_jogo:
    #------------------------------------------------------------------------------------------------------------------------#
        while(quemJoga == '2'): # enquanto o cliente joga 
            tabuleiro(frame_t1, tabuleiro_proprio, False, 0)
            separador(frame_separa, 11, 13)
            tabuleiro(frame_t2, tabuleiro_oponente, True, 11)
            jogar(frame_joga, "Atacar!") # recebe jogada

            # jogada = jogada(tabuleiro_oponente) 

            while validaJogada(tabuleiro_oponente,jogada) == False : # repete até jogada ser válida
                jogada = jogar(frame_joga, "Digite uma jogada válida.") # recebe jogada

            if not jogada or jogada == "sair" or jogada == "SAIR": # verifica se esse jogador deseja sair
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
                    sucesso = executarTiro(tabuleiro_proprio, jogada) # verifica a jogada do adversário

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
    client()