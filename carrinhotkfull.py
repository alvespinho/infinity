from tkinter import *
import json
from datetime import datetime


carrinho = []

def add_produto(produto, preco, und):
    carrinho.append({'Produto': produto, 'Preço': preco, 'Unidades': und})

def del_produto(produto):
    global carrinho 
    for item in carrinho:
        if item['Produto'] == produto:
            carrinho.remove(item)
            break

def ver_carrinho():
    total_preco = 0
    carrinho_text.set("### CARRINHO DE COMPRAS ###\n\n")
    for item in carrinho:
        produto = item['Produto']
        preco = item['Preço']
        und = item['Unidades']
        total_preco += preco * und
        carrinho_text.set(carrinho_text.get() + f"{produto.upper()} | ${preco:.2f} | {und} un\n")
    carrinho_text.set(carrinho_text.get() + f'\n###### TOTAL: ${total_preco:.2f} #####')

def show_error(message):
    resultado_label.config(text=message, fg='red')

def inserir_produto():
    produto = produto_entry.get()
    preco_entry_value = preco_entry.get()
    und_entry_value = und_entry.get()

    try:
        preco = float(preco_entry_value)
        und = int(und_entry_value)

        if preco <= 0 or und <= 0:
            show_error("Erro. Digite valores válidos.")
        else:
            add_produto(produto, preco, und)
            resultado_label.config(text=f"{und} {produto.upper()} foi adicionado ao carrinho!", fg='green')
            ver_carrinho()
            produto_entry.delete(0, END)
            preco_entry.delete(0, END)
            und_entry.delete(0, END)

    except ValueError:
        show_error("Erro! Digite valores válidos.")

def remover_produto():
    produto = produto_remover_entry.get()

    if not produto:
        show_error("Digite o nome do produto a ser removido!")
        return

    if not any(item['Produto'] == produto for item in carrinho):
        show_error(f"Erro! {produto} não encontrado no carrinho!")
        return

    del_produto(produto)
    resultado_label.config(text=f"{produto.upper()} foi removido do carrinho.")
    ver_carrinho()
    produto_remover_entry.delete(0, END)

def save_to_json():
    if not carrinho:
        show_error("Carrinho vazio! Adicione produtos antes de salvar.")
        return
    
    timestamp = datetime.now().strftime("%m%d")
    filename = f'carrinho_{timestamp}.json'
    
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(carrinho, json_file, ensure_ascii=False)
        resultado_label.config(text=f"Carrinho salvo em {filename}", fg='green')
    except Exception as e:
        resultado_label.config(text=f"Erro ao salvar o carrinho: {str(e)}", fg='red')

janela = Tk()

cor0 = "#000000"  # Black
cor1 = "#001F3F"  # Navy
cor2 = "#003366"  # Dark Navy
cor3 = "#004080"  # Deep Navy
cor4 = "#00509E"  # Rich Navy
cor5 = "#0066CC"  # Medium Blue
cor6 = "#0077CC"  # Bright Navy
cor7 = "#0088CC"  # Sky Blue
cor8 = "#0099CC"  # Cerulean Blue
cor9 = "#00AACC"  # Azure Blue
cor10 = "#00BBCC"  # Deep Sky Blue
cor11 = "#00CCCC"  # Light Blue
cor12 = "#FFFFFF"  # White


janela.title("Carrinho de Compras")
janela.geometry('350x920')
janela.resizable(width=False, height=False)
janela.config(bg=cor7)
janela.iconphoto(False, PhotoImage(file='shopping-cart.png'))


# Widgets
produto_label = Label(janela, text="Produto:", font=('Helvetica, 15 bold'), bg=cor7, relief='flat', fg= cor12)
produto_entry = Entry(janela)

preco_label = Label(janela, text="Preço:", font=('Helvetica, 15 bold'), bg=cor7, relief='flat', fg= cor12)
preco_entry = Entry(janela)

und_label = Label(janela, text="Unidades:", font=('Helvetica, 15 bold'), bg=cor7, relief='flat', fg= cor12)
und_entry = Entry(janela)

inserir_button = Button(janela, text="Inserir Produto", command=inserir_produto, font=('Helvetica, 12 bold'), bd=7,  relief='ridge')

produto_remover_label = Label(janela, text="Produto a remover:", font=('Helvetica, 15 bold'), bg=cor7, relief='flat', fg= cor12)
produto_remover_entry = Entry(janela)

remover_button = Button(janela, text="Remover Produto", command=remover_produto, font=('Helvetica, 12 bold'), bd=7,  relief='ridge')

# ver_carrinho_button = Button(janela, text="Ver Carrinho", command=ver_carrinho, font=('Helvetica, 12 bold'), bd=7,  relief='ridge')

resultado_label = Label(janela, font=('Helvetica, 9 italic bold'), bg=cor7, relief='flat')

carrinho_text = StringVar()
carrinho_text.set("### CARRINHO DE COMPRAS ###")
carrinho_label = Label(janela, textvariable=carrinho_text, font=('Helvetica, 10 bold'), fg= 'white', bd=7, bg='blue', relief='raised')


# Layout
produto_label.grid(row=0, column=0)
produto_entry.grid(row=0, column=1)
preco_label.grid(row=1, column=0)
preco_entry.grid(row=1, column=1)
und_label.grid(row=2, column=0)
und_entry.grid(row=2, column=1)
inserir_button.grid(row=4, column=0, columnspan=2, pady=(10, 0))

produto_remover_label.grid(row=6, column=0, pady=(10, 0))
produto_remover_entry.grid(row=6, column=1, pady=(10, 0))
remover_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

# ver_carrinho_button.grid(row=17, column=1, columnspan=2)
carrinho_label.grid(row=12, column=0, columnspan=2, pady=(10, 0))
resultado_label.grid(row=15, column=0, columnspan=2, pady=(10, 0))

# Add a new button to your GUI for saving to JSON
salvar_button = Button(janela, text="Salvar Carrinho", command=save_to_json, font=('Helvetica, 12 bold'), bd=7, relief = 'ridge')
salvar_button.grid(row=20, column=0, columnspan=2, pady=(10, 0)) 

janela.mainloop()
