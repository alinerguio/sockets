class Inserir_Navio:
	def __init__(self):


	def inserir(f, i, lista, r, c):
	color = corCelula(i)
	l = []
	if len(lista) == 0:
		botao = Button(f, text = i, command = lambda: l=inserir_navio(lista, [r, c]), bg=color)
	elif len(lista) == 1:
		if r == lista[0][0]:  
			botao = Button(f, text = i, command = lambda: l=inserir_navio(lista, [r, c]), bg=color)
		elif c == lista[0][1]:
			botao = Button(f, text = i, command = lambda: l=inserir_navio(lista, [r, c]), bg=color)
		else:
			botao = Button(f, text = i, bg=color, state=DISABLED)

	botao.grid(row=r, column=c)

	return l
	
def inserir_navio(lista, rc):
	lista.append(rc)
	print(lista) 
	return lista