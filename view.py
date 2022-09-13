import sys
import tkinter as tk
from tkinter import *
import tkinter.messagebox


class View():
    def __init__(self, info=None):
        # Inicializando o tkinter
        self.root = tk.Tk()

        # Estilizando
        self.root.title("Jogo da Velha - MVC")
        self.root.geometry("300x200")
        self.root.configure(background="black")

        # Iniciando a interface
        self.x = 0  # indice da variavel de criar o jogo
        self.startGame()

        self.name1 = ""
        self.name2 = ""

        # Clicar na tecla ESC e sair
        self.root.bind('<Escape>', self.close)

    def startGame(self):
        # Informacoes do jogo
        info = tk.Frame(self.root)
        info.pack()
        info.configure(bg='black')

        # Header
        self.labelTitulo = tk.Label(info,
                                    height=4,
                                    text="Jogo da Velha",
                                    bg='black',
                                    fg='white')
        self.labelTitulo.pack(side='top')

        # Players
        players = tk.Frame(self.root)
        players.pack()
        players.configure(bg='black')

        self.labP1 = tk.Label(players,
                              text="Jogador 1 (X)",
                              bg='black',
                              fg='white')
        self.labP1.grid(row=0, column=0)

        self.player1 = tk.Entry(players,
                                bd=3)
        self.player1.grid(row=0, column=1)

        self.labP2 = tk.Label(players,
                              text="Jogador 2 (O)",
                              height=2,
                              bg='black',
                              fg='white')
        self.labP2.grid(row=1, column=0)

        self.player2 = tk.Entry(players,
                                bd=3)
        self.player2.grid(row=1, column=1)

        # Gerador da interface
        start = tk.Frame(self.root)
        start.pack()
        start.configure(bg='black')

        self.invisibleRow1 = tk.Label(start,
                                      height=1,
                                      bg='black')
        self.invisibleRow1.pack()

        self.btnStart = tk.Button(start,
                                  width=15,
                                  text='Começar Jogo',
                                  command=self.generateGame)
        self.btnStart.pack()

        self.invisibleRow2 = tk.Label(start,
                                      height=1,
                                      bg='black')
        self.invisibleRow2.pack()

    # Interface
    def interface(self):
        # Jogo
        container = tk.Frame(self.root)
        container.pack()

        self.button1 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick1)
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick2)
        self.button2.grid(row=0, column=1)

        self.button3 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick3)
        self.button3.grid(row=0, column=2)

        self.button4 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick4)
        self.button4.grid(row=1, column=0)

        self.button5 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick5)
        self.button5.grid(row=1, column=1)

        self.button6 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick6)
        self.button6.grid(row=1, column=2)

        self.button7 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick7)
        self.button7.grid(row=2, column=0)

        self.button8 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick8)
        self.button8.grid(row=2, column=1)

        self.button9 = tk.Button(container,
                                 width=15,
                                 height=10,
                                 text='',
                                 bg='grey',
                                 fg='white',
                                 command=self.executeClick9)
        self.button9.grid(row=2, column=2)

    # Gerando a interface
    def generateGame(self):
        # Passando o nome dos jogadores
        self.name1 = self.player1.get()
        self.name2 = self.player2.get()
        # Passando pro controller
        self.controller.namePlayers(self.name1, self.name2)
        # Iniciando o tabuleiro
        if (self.x == 0):
            self.interface()
            self.root.geometry("600x700")
            self.x = 1
        else:
            tkinter.messagebox.showinfo(
                "ERRO", "Jogo já criado!", icon='error')

    # Chamando o controller
    def setController(self, controller):
        self.controller = controller

    # Manter em loop
    def run(self):
        self.root.mainloop()

    # METODOS DO CLICK DE CADA BOTAO

    # BOTAO 1
    def executeClick1(self):
        self.controller.clickField1()

    # Mudar o texto do botão
    def setButtonText1(self, text):
        self.button1['text'] = text

    # BOTAO 2
    def executeClick2(self):
        self.controller.clickField2()

    def setButtonText2(self, text):
        self.button2['text'] = text

    # BOTAO 3
    def executeClick3(self):
        self.controller.clickField3()

    def setButtonText3(self, text):
        self.button3['text'] = text

    # BOTAO 4
    def executeClick4(self):
        self.controller.clickField4()

    def setButtonText4(self, text):
        self.button4['text'] = text

    # BOTAO 5
    def executeClick5(self):
        self.controller.clickField5()

    def setButtonText5(self, text):
        self.button5['text'] = text

    # BOTAO 6
    def executeClick6(self):
        self.controller.clickField6()

    def setButtonText6(self, text):
        self.button6['text'] = text

    # BOTAO 7
    def executeClick7(self):
        self.controller.clickField7()

    def setButtonText7(self, text):
        self.button7['text'] = text

    # BOTAO 8
    def executeClick8(self):
        self.controller.clickField8()

    def setButtonText8(self, text):
        self.button8['text'] = text

    # BOTAO 9
    def executeClick9(self):
        self.controller.clickField9()

    def setButtonText9(self, text):
        self.button9['text'] = text

    # Fechar velha
    def close(self, evento=None):
        sys.exit()
