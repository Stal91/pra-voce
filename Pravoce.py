import tkinter as tk
import random

# função para mudar a posição do botão


# função para quando o botão "Sim" é clicado
def sim_clicado():
    mensagem.config(text="TE AMO LINDA")

# função para quando o botão "Não" é clicado
def nao_clicado():
    x = random.randint(0, largura - tamanho)
    y = random.randint(0, altura - tamanho)
    nao_botao.place(x=x, y=y)

# criação da janela principal
janela = tk.Tk()
janela.title("FICA COMIGO PRA SEMPRE")




# definindo o tamanho da janela
largura = 400
altura = 400
janela.geometry(f"{largura}x{altura}")

# criação do botão
tamanho = 50


# criação dos botões "Sim" e "Não"
sim_botao = tk.Button(janela, text="Sim", command=sim_clicado)
nao_botao = tk.Button(janela, text="Não", command=nao_clicado)
sim_botao.place(x=largura//2 - 50, y=altura//2 + 50)
nao_botao.place(x=largura//2 + 50, y=altura//2 + 50)

# criação do elemento de mensagem
mensagem = tk.Label(janela, text="")
mensagem.place(x=50, y=100)

# loop principal da janela
janela.mainloop()
