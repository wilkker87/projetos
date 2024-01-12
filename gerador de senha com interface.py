from tkinter import *
import random
import string

janela = Tk()

janela.title("Gerador de Senhas")
janela.geometry("300x200")

botao = Button(janela, text="Gerar Senha")
texto = Label(janela, text="Digite o tamanho da senha:")
texto2 = Label(janela, text="Nova senha aleatória:")
entrada = Entry(janela)
saida = Entry(janela) # cria um widget de entrada para mostrar a senha

botao.pack()
texto.pack()
entrada.pack()
texto2.pack()
saida.pack() # adiciona o widget de entrada na janela

def gerar_senha():
    # Verifica se a caixa de texto é válida
    if entrada.get() == "" or not entrada.get().isdigit():
        # Exibe uma mensagem de erro
        saida.delete(0, END) # apaga o conteúdo anterior do widget de entrada
        saida.insert(0, "Erro: digite um número inteiro.") # insere a mensagem de erro no widget de entrada
    if entrada.get() == "0" or not entrada.get().isdigit():
        # Exibe uma mensagem de erro
        saida.delete(0, END) # apaga o conteúdo anterior do widget de entrada
        saida.insert(0, "Erro: digite um número inteiro.") # insere a mensagem de erro no widget de entrada
    else:
        # Gera uma senha aleatória
        tamanho = int(entrada.get())
        senha = ""
        for i in range(tamanho):
            senha += random.choice(string.ascii_letters + string.digits + string.digits + "!")
        saida.delete(0, END) # apaga o conteúdo anterior do widget de entrada
        saida.insert(0, senha) # insere a senha no widget de entrada
        saida.get() # obtém o valor da senha

botao["command"] = gerar_senha

janela.mainloop()