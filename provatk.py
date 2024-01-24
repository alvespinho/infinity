from tkinter import *
from tkinter import Tk, messagebox

# CORES
cor1 = "black"
cor2 = "white"
cor3 = "blue"

#FUNÇÕES
def cm_para_m():
    try:
        centimeter = float(entry.get())
        meter = centimeter / 100
        result_label.config(text=f'Resultado: {centimeter} cm = {meter:.2f} metros', fg=cor1)
    except ValueError:
        messagebox.showerror("Erro!", "Digite um número válido.")

## CRIANDO JANELA ##
janela = Tk()
janela.title('Conversor de Medidas')
janela.geometry('310x300')
janela.config(bg=cor2)
janela.resizable(width=FALSE, height=FALSE)

## DIVIDINDO JANELA ##
frame_decima = Frame(janela, width=310, height=50, bg=cor2, relief='flat')
frame_decima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_debaixo = Frame(janela, width=310, height=250, bg=cor2, relief='flat')
frame_debaixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

## FRAME DE CIMA ##
login_nome = Label(frame_decima, text='Conversor de Medidas', anchor=NE, font=('Ivy 14'), bg=cor2, fg=cor1)
login_nome.place(x=5, y=5)

## SEPARADOR ##
separador = Label(frame_decima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=cor3, fg=cor2)
separador.place(x=10, y=45)

## ENTRADA DE DADOS ##
entry_label = Label(frame_debaixo, text='Centímetros: ', font=('Ivy 10'), bg=cor2, fg=cor1)
entry_label.place(x=20, y=30)

entry = Entry(frame_debaixo, width=20, font=('Ivy 10'))
entry.place(x=110, y=30)

## BOTÃO DE CONVERSÃO ##
convert_button = Button(frame_debaixo, text='Converter', command=cm_para_m, font=('Ivy 10'), bg=cor3, fg=cor2)
convert_button.place(x=130, y=70)

## RESULTADO ##
result_label = Label(frame_debaixo, text='Resultado: ', font=('Ivy 10'), bg=cor2, fg=cor1)
result_label.place(x=20, y=110)

janela.mainloop()
