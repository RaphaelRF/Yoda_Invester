import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import investpy
from tkinter import *
import tkinter.font as tkFont

v_n = 'NULL'
v_s = 'NULL'
v_e = 'NULL'

def pega_nomes(vnome,vstart,vend):
    global v_n
    global v_s
    global v_e

    v_n = vnome.get()
    v_s = vstart.get()
    v_e = vend.get()

def action():
    pega_nomes(vnome, vstart, vend)
    janela.destroy()

    janela1 = Tk()
    janela1.title("Yoda Investor")

    posx1 = (janela1.winfo_screenwidth() / 2) - 215
    posy1 = (janela1.winfo_screenheight() / 2) - 90

    janela1.geometry("430x180+%d+%d" % (posx1, posy1))
    janela1.configure(background="#dde")

    # Máxima
    botao1 = Button(janela1, text="Valor Máximo", command=Maxima)
    botao1.place(x=20, y=30, width=170, height=50)

    # Mínimo
    botao2 = Button(janela1, text="Valor Mínimo", command=Minima)
    botao2.place(x=235, y=30, width=170, height=50)

    # Fechamento
    botao3 = Button(janela1, text="Fechamento", command=Fechamento)
    botao3.place(x=20, y=100, width=170, height=50)

    # Volume
    botao4 = Button(janela1, text="Volume", command=Volume)
    botao4.place(x=235, y=100, width=170, height=50)

    janela1.mainloop()

def Maxima ():
    dado = 'High'
    #Money(vnome.get(), vstart.get(), vend.get(), dado)
    Money(v_n, v_s, v_e, dado)

def Minima ():
    dado = 'Low'
    #Money(vnome.get(), vstart.get(), vend.get(), dado)
    Money(v_n, v_s, v_e, dado)
def Fechamento ():
    dado = 'Close'
    #Money(vnome.get(), vstart.get(), vend.get(), dado)
    Money(v_n, v_s, v_e, dado)
def Volume ():
    dado = 'Volume'
    #Money(vnome.get(), vstart.get(), vend.get(), dado)
    Money(v_n, v_s, v_e, dado)

def Money (nome_acao, start, end, dado):
    result = investpy.search_quotes(text = nome_acao, products=['stocks'], countries = ['brazil'], n_results=1)

    data = result.retrieve_historical_data(from_date= start, to_date= end)
    plt.plot(data[dado])
    plt.title(nome_acao)
    plt.ylabel('Valor')
    plt.xlabel('Período')
    plt.show()

#Layout do programa

#Config inicial
janela = Tk()
janela.title("Yoda Investor")

posx = (janela.winfo_screenwidth()/2) - 215
posy = (janela.winfo_screenheight()/2) - 150

janela.geometry("430x300+%d+%d" % (posx,posy))
janela.configure(background="#dde")

#Imagem com texto
img = PhotoImage(file="yoda.png")

yoda = Label(janela, image=img)
yoda.place(x=10, y=10)
texto = Label(janela, text = "Investir você deve", font = tkFont.Font(family="Lucida Grande", size=20))
texto.place(x=10, y=250)

#Nome da ação
Nome = Label(janela, text="Nome da ação", background="#dde", foreground="#009", font = tkFont.Font(family="Lucida Grande", size=15))
Nome.place(x=250, y=10)
vnome = Entry(janela)
vnome.place(x=255, y=40)

#Periodo 1
Start = Label(janela, text="Start (dd/mm/yyyy)", background="#dde", foreground="#009",
             font=tkFont.Font(family="Lucida Grande", size=15))
Start.place(x=250, y=70)
vstart = Entry(janela)
vstart.place(x=255, y=100)

#Periodo 2
End = Label(janela, text="End (dd/mm/yyyy)", background="#dde", foreground="#009",
             font=tkFont.Font(family="Lucida Grande", size=15))
End.place(x=250, y=130)
vend = Entry(janela)
vend.place(x=255, y=160)

#botao
botao = Button(janela, text="SHOW ME THE MONEY", command=action)
botao.place(x=250, y=220, width=170, height=50)

janela.mainloop()



