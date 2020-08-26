from tkinter import *

def insere(frame_joga, frame_t1, tabuleiro_1, lista_navios):
	if lista_navios == []:
		tabuleiro(frame_t1, tabuleiro_1, False, 0)
		jogar(frame_joga, "Aguarde o outro jogador.")
	elif lista_navios != []:
		inserir_navios(frame_joga, lista_navios[0][0], lista_navios[0][1])
		main_inserir(frame_t1, tabuleiro_1, [], lista_navios[0][1], lista_navios, frame_joga)


def main_inserir(f, tabuleiro, lista, tamanho_navio, lista_navios, frame_joga):
	r = 0
	for linha in tabuleiro:
		c = 0
		for i in linha:
			inserir(f, tabuleiro, i, lista, tamanho_navio, r, c, lista_navios, frame_joga)
			c += 1 
		r += 1
		
def inserir(f, tab, i, lista, tamanho_navio, r, c, lista_navios, frame_joga):
	color = corCelula(i)

	if (i == '-'):
		if len(lista) == 0: # disponibiliza todos para serem clicados
			botao = Button(f, text = i, height = 2, width = 3, command = (lambda: inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)), bg=color, state=NORMAL)
			botao.grid(row=r, column=c)
		elif len(lista) == 1: # disponibiliza somente as possíveis colunas e linhas para ser inserido o navio (vertical ou horizontal)
			
			if r == lista[0][0] and (c == (lista[0][1] + 1) or c == (lista[0][1] - 1)): # se tem mesma linha e é um após  
				botao = Button(f, text = i, height = 2, width = 3, command = (lambda: inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)), bg=color)
				botao.grid(row=r, column=c)
			elif c == lista[0][1] and (r == (lista[0][0] + 1) or r == (lista[0][0] - 1)): # se tem mesma coluna e é um após
				botao = Button(f, text = i, height = 2, width = 3, command = (lambda: inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)), bg=color)
				botao.grid(row=r, column=c)
			elif r == lista[0][0] and c == lista[0][1]: # desativa ele mesmo para clique
				botao = Button(f, text = 'X', height = 2, width = 3, bg=color, state=DISABLED)
				botao.grid(row=r, column=c)
			else:
				botao = Button(f, text = i, height = 2, width = 3, bg=color, state=DISABLED)
				botao.grid(row=r, column=c)
		elif len(lista) > 1:
			inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)
	else:
		botao = Button(f, text = i, height = 2, width = 3, bg=color, state=DISABLED)
		botao.grid(row=r, column=c)
	

# puxar TODAS verificações para interface
def inserir_celula(lista, celula, tamanho_navio, f, tab, lista_navios, frame_joga):
	if len(lista) == 0: # primeiro é livre para inserir onde quiser 
		lista.append(celula)
		main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

	elif len(lista) == 1: # a depender do tamanho do navio
		if tamanho_navio == 2:
			lista.append(celula)
			inserir_tabuleiro(tab, lista, tamanho_navio, f, lista_navios, frame_joga)

		elif tamanho_navio == 3:
			if (celula[0] <= 8 or celula[1] <= 8):
				lista.append(celula)
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

			elif (lista[0][0] > celula[0] or lista[0][1] > celula[1]):
				lista.append(celula)
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

			else:
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)
				print("deu errado, navio grande")

		elif tamanho_navio == 4:

			if (celula[0] <= 7 or celula[1] <= 7):
				lista.append(celula)
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

			elif (lista[0][0] > celula[0] or lista[0][1] > celula[1]): 
				lista.append(celula)
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

			else:
				main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)
				print("deu errado, navio grande - try again baby")

	elif len(lista) < tamanho_navio: # insere o resto do navio
		inserir_navio(lista, tamanho_navio, f, tab, lista_navios, frame_joga)

def inserir_navio(lista, tam, f, tab, lista_navios, frame_joga):
	if lista[0][0] == lista[1][0]:  # mesma linha
		if lista[0][1] < lista[1][1]: # inserir em sentido para baixo ou para direita
			a = lista[1][1] + 1
			for i in range(a, a+tam-2):
				lista.append([lista[0][0], i])
		else: # inserir em sentido para cima ou para esquerda
			a = lista[0][1] - 1
			for i in range(a-tam+2, a):
				lista.append([lista[0][0], i])

		inserir_tabuleiro(tab, lista, tam, f, lista_navios, frame_joga)

	elif lista[0][1] == lista[1][1]: # mesma coluna
		if lista[0][0] < lista[1][0]: # inserir em sentido para baixo ou para direita
			a = lista[1][0] + 1
			for i in range(a, a+tam-2):
				lista.append([i, lista[0][1]])
		else: # inserir em sentido para cima ou para esquerda
			a = lista[0][0] - 1
			for i in range(a-tam+2, a):
				lista.append([i, lista[0][1]])

		inserir_tabuleiro(tab, lista, tam, f, lista_navios, frame_joga)

# após todas verificações, insere no tabuleiro 
def inserir_tabuleiro(tab, lista, tam, f, lista_navios, frame_joga):
	b = True
	for i in lista: # insere
		r = i[0]
		c = i[1]
		if tab[r][c] == 'X':
			b = False
	if b:
		lista_navios.remove(lista_navios[0])
		for i in lista: # insere
			r = i[0]
			c = i[1]
			tab[r][c] = 'X'
		status(frame_joga, "Inserir o navio:")
		insere(frame_joga, f, tab, lista_navios)
	else:
		status(frame_joga, "Já existe algum navio inserido nessa posição, tente novamente!")
		insere(frame_joga, f, tab, lista_navios)

def corCelula(i):
	if i == 'X':
		return "red"
	elif i == 'O':
		return "black"
	elif i == '.':
		return "blue"
	else:
		return "grey"

# exibe o botao ativado ou desativado de acordo com os parâmetros
def exibir_botao(f, i, b, r, c):  
	color = corCelula(i)

	if b:  
		botao = Button(f, text = i, bg=color, state=NORMAL, height = 2, width = 3)
	else: 
		botao = Button(f, text = i, bg=color, state=DISABLED, height = 2, width = 3)

	botao.grid(row=r, column=c)
    
# printar o tabuleiro
def tabuleiro(f, tabuleiro, b, c):
	r = 0
	for linha in tabuleiro:
		c1 = c
		for i in linha:
			exibir_botao(f, i, b, r, c1)
			c1 += 1 
		r += 1

# separador na interface dos dois tabuleiros
def separador(frame_separa, c, l):
	for i in range(l):
		w = Label(frame_separa, text="|")
		w.grid(row=i, column=c)

# mensagens ao longo do jogo no rodapé 

# instruções
##### FAZER 

#especifica o tamanho do navio a ser inserido e como 
def inserir_navios(frame_joga, nome, tamanho):
	frame_joga.grid_forget() 
	frame_joga.grid(rowspan=5, sticky=SW, pady=20, padx=5)
	label = Label(frame_joga, text="Selecione onde o " + nome + " de tamanho " + str(tamanho) + " irá ser inserido", font=("Courier", 15))
	label.grid(sticky=W, row=2)
# status do jogo/instrução do que o jogador deve fazer 
def status(frame_joga, status):
	Label(frame_joga, text=status, font=("Courier", 20)).grid(sticky=W, row=0)

# status do jogo/instrução do que o jogador deve fazer 
def jogar(frame_joga, status):
	Label(frame_joga, text=status, font=("Courier", 20)).grid(sticky=W, row=0)
	botao = Button(frame_joga, text = "Sair", command = sair)
	botao.grid(sticky=E)

#função para sair do jogo 
def sair():
	print("sair")

#mensagem de fim de jogo
def fim(frame_joga, mensagem):
	Label(frame_joga, text=mensagem, font=("Courier", 40)).grid(sticky=W)





