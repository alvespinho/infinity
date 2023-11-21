from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
import os
import platform
import os
import platform
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


DIR_PATH = os.getcwd()
SESSION_NAME = 'Wtsp'
USER_LOGIN = os.getlogin()

if platform.system() == 'Windows':
    CHROME_PROFILE_PATH = \
        f"user-data-dir=C:\\Users\\{USER_LOGIN}\\AppData\\Local\\Google\\Chrome\\{SESSION_NAME}"
else:
    CHROME_PROFILE_PATH = \
        f'user-data-dir=/home/{USER_LOGIN}/.config/google-chrome/{SESSION_NAME}'

CHROME_OPTIONS = Options()
CHROME_OPTIONS.add_argument(CHROME_PROFILE_PATH)

CHROME_DRIVER_PATH = os.path.join(DIR_PATH, 'chromedriver.exe')
CHROME_SERVICE = Service(executable_path = CHROME_DRIVER_PATH)



class ChatApplication:
    def __init__ (self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=700, height=500, bg=BG_COLOR)

        #CABEÇALHO
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR, 
                            text="Bem Vindo!", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider 
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight= 0.012)

        contatos = list(pd.read_excel('contatos.xlsx')['CONTATOS'])

        self.tamanho = Label(self.window, text=f'Seu arquivo tem {len(contatos)} números', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD, pady=10)
        self.tamanho.place(relwidth=1, rely=0.08, relheight= 0.1)
        
        #LISTA COM OS CONTATOS EXIBIDOS
        listaDeContatos = Variable(value=contatos)
        self.listaContatos = Listbox(self.window, height = 3, listvariable = listaDeContatos, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD)
        self.listaContatos.place(relwidth=1, rely=0.2, relheight= 0.15)

        self.messageTitle = Label(self.window, text=f'Digite o conteúdo da mensagem: ', bg=BG_COLOR, fg=TEXT_COLOR, font=FONT_BOLD, pady=5)
        self.messageTitle.place(relwidth=1, rely=0.45, relheight= 0.1)
        self.text_widget = Entry(self.window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.text_widget.place(relheight=0.3, relwidth=1, rely=0.55)
        self.text_widget.configure(cursor="arrow")

        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.80)

        self.msg_entry = Text(self.text_widget, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=1, relheight=1, bordermode=INSIDE)
        # self.msg_entry.focus()
        #self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Enviar", font=FONT_BOLD, width=20, bg=BG_GRAY, command=self.automacao_mensagens)
        send_button.place(relheight=0.06, relwidth=1)
    
    def automacao_mensagens(self):
        try:
            navegador = webdriver.Chrome(service=CHROME_SERVICE)
            navegador.get("https://web.whatsapp.com/")

            mensagem = self.msg_entry.get("1.0","end-1c")
            contatos = list(pd.read_excel('contatos.xlsx')['CONTATOS'])
            nomes =  list(pd.read_excel('contatos.xlsx')['NOMES'])


            while len(navegador.find_elements(by=By.ID,value="side")) < 1:
                time.sleep(1)

            # já estamos com o login feito no whatsapp web
            for i in range(len(contatos)):
                pessoa = nomes[i]
                numero = contatos[i]
                texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
                link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
                navegador.get(link)
                while len(navegador.find_elements(by=By.ID,value="side")) < 1:
                    time.sleep(1)
                navegador.find_element(by=By.XPATH, value='/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').send_keys(Keys.ENTER)
                time.sleep(10)
        finally:
            navegador.quit()

if __name__ == "__main__":
    app = ChatApplication()
    app.run()