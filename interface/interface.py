from tkinter import *

def cria_janela(menu, nome):
    menu.title("Batalha Naval - " + nome)
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

    w = Label(frame_labels, text="Meu Jogo", font=("Courier", 20))
    w.grid(row=0, column=5, padx=150, pady=10)
    w = Label(frame_labels, text="Jogo Rival", font=("Courier", 20))
    w.grid(row=0, column=20, padx=150, pady=10)

    frames = [frame_t1, frame_separa, frame_t2, frame_joga]

    return frames

def cria_tabuleiro():
    novoTabuleiro = []
    for _ in range(10):
        novoTabuleiro.append(['-','-','-','-','-','-','-','-','-', '-'])
    return novoTabuleiro

def navios():
	return [["porta aviao", 2], ["submarino", 2], ["foguete", 3], ["navio tanque", 3], ["contra torpedo", 4], ["contra torpedo", 4]]

def insere(frame_joga, frame_t1, tabuleiro_1, lista_navios):
	
	if lista_navios == []:
		tabuleiro(frame_t1, tabuleiro_1, False, 0)
		status(frame_joga, "Aguarde o outro jogador.")
		return True
	elif lista_navios != []:
		inserir_navios(frame_joga, lista_navios[0][0], lista_navios[0][1])
		main_inserir(frame_t1, tabuleiro_1, [], lista_navios[0][1], lista_navios, frame_joga)
		return False

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
			b = True 

			if tamanho_navio > 2: # para desativar aqueles que serão muito na borda
				# verificação de linha

				# se for maior
				if r > (11 - tamanho_navio) and r > lista[0][0]: 
					b = False

				#se for menor
				if r < (tamanho_navio - 2) and r < lista[0][0]: 
					b = False

				# verificação de coluna 

				# se for maior
				if c > (11 - tamanho_navio)and c > lista[0][1]: 
					b = False

				# se for menor
				if c < (tamanho_navio - 2) and c < lista[0][1]: 
					b = False


			if r == lista[0][0] and (c == (lista[0][1] + 1) or c == (lista[0][1] - 1)) and b: # se tem mesma linha e é um após  
				botao = Button(f, text = i, height = 2, width = 3, command = (lambda: inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)), bg=color)
				botao.grid(row=r, column=c)

			elif c == lista[0][1] and (r == (lista[0][0] + 1) or r == (lista[0][0] - 1)) and b: # se tem mesma coluna e é um após
				botao = Button(f, text = i, height = 2, width = 3, command = (lambda: inserir_celula(lista, [r, c], tamanho_navio, f, tab, lista_navios, frame_joga)), bg=color)
				botao.grid(row=r, column=c)

			elif r == lista[0][0] and c == lista[0][1]: # desativa ele mesmo para clique
				botao = Button(f, text = 'X', height = 2, width = 3, bg=color, state=DISABLED)
				botao.grid(row=r, column=c)

			else: # todo o resto deve ser desativado 
				botao = Button(f, text = i, height = 2, width = 3, bg=color, state=DISABLED)
				botao.grid(row=r, column=c)

	else:
		botao = Button(f, text = i, height = 2, width = 3, bg=color, state=DISABLED)
		botao.grid(row=r, column=c)
	

# puxar TODAS verificações para interface
def inserir_celula(lista, celula, tamanho_navio, f, tab, lista_navios, frame_joga):
	if len(lista) == 0: # primeiro é livre para inserir onde quiser 
		lista.append(celula)
		main_inserir(f, tab, lista, tamanho_navio, lista_navios, frame_joga)

	elif len(lista) == 1: 
		lista.append(celula) # insere o segundo do navio
		inserir_navio(lista, tamanho_navio, f, tab, lista_navios, frame_joga)

def inserir_navio(lista, tam, f, tab, lista_navios, frame_joga):
	if lista[0][0] == lista[1][0]:  # mesma linha

		if lista[0][1] < lista[1][1]: # inserir em sentido para baixo ou para direita
			a = int(lista[1][1]) + 1
			for i in range(a, a+tam-2):
				lista.append([lista[0][0], i])
		else: # inserir em sentido para cima ou para esquerda
			a = int(lista[0][1]) - 1
			for i in range(a-tam+2, a):
				lista.append([lista[0][0], i])
		inserir_tabuleiro(tab, lista, tam, f, lista_navios, frame_joga)

	elif lista[0][1] == lista[1][1]: # mesma coluna

		if lista[0][0] < lista[1][0]: # inserir em sentido para baixo ou para direita
			a = int(lista[1][0]) + 1
			for i in range(a, a+tam-2):
				lista.append([i, lista[0][1]])
		else: # inserir em sentido para cima ou para esquerda
			a = int(lista[0][0]) - 1
			for i in range(a-tam+2, a):
				lista.append([i, lista[0][1]])
		inserir_tabuleiro(tab, lista, tam, f, lista_navios, frame_joga)

# insere no tabuleiro somente se verificar que pode 
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
	else: # pode ser verificado na interface - se der tempo -> fazer 
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

#executa o tiro do jogo
def executar_tiro(tabuleiro, posicao):
    linha = posicao[0]
    coluna = posicao[1]
    if tabuleiro[int(linha)][int(coluna)] == 'O':
        tabuleiro[int(linha)][int(coluna)] == 'X'
        return True
    else:
        tabuleiro[int(linha)][int(coluna)] == '.'
        return False

# printar o tabuleiro
def tabuleiro_ataque(f, tabuleiro, c, tiro):
	while c != -1:
		tabuleiro(f, tabuleiro, True, c)

	if tiro[0] == -1: 
		return 'sair'
	else: 
		return tiro

# exibe o botao ativado ou desativado de acordo com os parâmetros
def exibir_botao(f, i, b, r, c, tabuleiro):  
	color = corCelula(i)

	if b or i == '-':  
		botao = Button(f, text = i, bg=color, state=NORMAL, command = lambda: tabuleiro_ataque(f, tabuleiro, -1, [r, c]), height = 2, width = 3)
	else: 
		botao = Button(f, text = i, bg=color, state=DISABLED, height = 2, width = 3)

	botao.grid(row=r, column=c)
    
# printar o tabuleiro
def tabuleiro(f, tabuleiro, b, c):
	r = 0
	for linha in tabuleiro:
		c1 = c
		for i in linha:
			exibir_botao(f, i, b, r, c1, tabuleiro)
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
def jogar(frame_joga, status, f, tabuleiro):
	Label(frame_joga, text=status, font=("Courier", 20)).grid(sticky=W, row=0)
	botao = Button(frame_joga, text = "Sair", command = lambda: tabuleiro_ataque(f, tabuleiro, -1, [-1, -1]))
	botao.grid(sticky=E)

#mensagem de fim de jogo
def fim(frame_joga, mensagem):
	Label(frame_joga, text=mensagem, font=("Courier", 40)).grid(sticky=W)





