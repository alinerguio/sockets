from tkinter import *
from regrasDoJogo import *
from interface import *

tabuleiro_1 = criaTabuleiro()
tabuleiro_2 = criaTabuleiro()

menu = Tk()
menu.title("Batalha Naval")
menu.geometry("850x600")

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

w = Label(frame_labels, text="Meu Jogo", font=("Courier", 20))
w.grid(row=0, column=5, padx=150, pady=10)
w = Label(frame_labels, text="Jogo Rival", font=("Courier", 20))
w.grid(row=0, column=20, padx=150, pady=10)

lista_navios = [["porta aviao", 2], ["submarino", 2], ["foguete", 3], ["navio tanque", 3], ["contra torpedo", 4], ["contra torpedo", 4]]

# inserir navios 
status(frame_joga, "Inserir o navio:")
insere(frame_joga, frame_t1, tabuleiro_1, lista_navios)

# printa o resto do tabuleiro
separador(frame_separa, 11, 16)
tabuleiro(frame_t2, tabuleiro_2, False, 11)


#jogar(frame_joga, "Clique na posição a ser atacada!")
#fim(frame_joga, "Você ganhou!")

menu.mainloop()
