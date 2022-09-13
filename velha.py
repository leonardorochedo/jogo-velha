from msilib.schema import Icon
from tkinter import *
import tkinter.messagebox


class Velha:
    def __init__(self) -> None:

        # Manipular os click para verificar o empate
        self.countDrawn = 0
        # O tabuleiro em si
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        # Um marcador para saber se alguem ganhou ou quem vai marcar
        self.markdown = 1
        # As jogadas
        self.markWithX = 'X'
        self.markWithO = 'O'
        self.listOfButtons = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # Players
        self.player1 = ''
        self.player2 = ''

    # Adicionando os jogadores
    def addPlayers(self, nameX, nameO):
        if (nameX == ''):
            self.player1 = 'Player 1'
        if (nameO == ''):
            self.player2 = 'Player 2'
        if (nameX != '' and nameO != ''):
            self.player1 = nameX
            self.player2 = nameO

    # Decidindo se jogue X ou O
    def choosePlayer(self, numButton):
        if (self.markdown == 1):
            if (self.buttonValid(numButton) == 1):
                self.markdown = 0
                self.countDrawn += 1  # Draw
                return self.markWithX
            else:
                tkinter.messagebox.showinfo(
                    "ERRO", "Esse botão já foi clicado!", icon='info')
                return self.markWithO

        if (self.markdown == 0):
            if (self.buttonValid(numButton) == 1):
                self.markdown = 1
                self.countDrawn += 1  # Draw
                return self.markWithO
            else:
                tkinter.messagebox.showinfo(
                    "ERRO", "Esse botão já foi clicado!", icon='info')
                return self.markWithX

    # Validar se o botão já foi clicado
    def buttonValid(self, numButton):
        if (numButton == self.listOfButtons[numButton-1]):
            self.listOfButtons[numButton-1] = 0  # Tirando o elemento da lista
            return 1
        else:
            return 0

    def winnerOfMatch(self):

        # Empate
        if self.countDrawn == 8:
            return 3

        # Quem ganhou em formato de linha
        for i in range(3):
            rowWin = self.board[i][0]+self.board[i][1]+self.board[i][2]
            if rowWin == 3:
                return 1
            elif rowWin == -3:
                return 2

        # Quem ganhou em formato de coluno
        for i in range(3):
            columnWin = self.board[0][i]+self.board[1][i]+self.board[2][i]
            if columnWin == 3:
                return 1
            elif columnWin == -3:
                return 2

        # Quem ganhou em formato de diagonal
        diagonalWin1 = self.board[0][0]+self.board[1][1]+self.board[2][2]
        diagonalWin2 = self.board[0][2]+self.board[1][1]+self.board[2][0]
        if diagonalWin1 == 3 or diagonalWin2 == 3:
            return 1
        elif diagonalWin1 == -3 or diagonalWin2 == -3:
            return 2
        return 0

    def addPlayTable(self, columnTable, rowTable):

        # Enquanto não tem um ganhador
        if self.winnerOfMatch() == 0:
            # Onde e oque será marcado
            if (self.markdown == 1):
                if (rowTable == 0):
                    # Se não foi clicado
                    self.board[0][columnTable] = 1
                if (rowTable == 1):
                    self.board[1][columnTable] = 1
                if (rowTable == 2):
                    self.board[2][columnTable] = 1
            else:
                if (rowTable == 0):
                    self.board[0][columnTable] = -1
                if (rowTable == 1):
                    self.board[1][columnTable] = -1
                if (rowTable == 2):
                    self.board[2][columnTable] = -1

        # Player 1 ganhou
        if self.winnerOfMatch() == 1:
            tkinter.messagebox.showinfo(
                "Vitória!", self.player1 + " ganhou o jogo!!", icon='info')
        # Player 2 ganhou
        if self.winnerOfMatch() == 2:
            tkinter.messagebox.showinfo(
                "Vitória!", self.player2 + " ganhou o jogo!!", icon='info')
        # Empate
        if self.winnerOfMatch() == 3:
            tkinter.messagebox.showinfo(
                "Empate!", "O jogo terminou em empate!!", icon='info')
