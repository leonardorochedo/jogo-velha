class Controller:
    def __init__(self, view, model) -> None:
        self.view = view
        self.model = model

    # Metodos dos cliques

    # Definindo o nome dos jogadores
    def namePlayers(self, nameX, nameO):
        # Passando os 2 nomes como parametro
        self.model.addPlayers(nameX, nameO)

    # Botão 1
    def clickField1(self):
        # Chamando e passando os parametros para a função que adiciona eles na tabela
        self.model.addPlayTable(0, 0)
        # Definindo se o que vai ir pro tabuleiro é X ou O
        move = self.model.choosePlayer(1)
        # Setando o conteúdo do botão na tabela
        self.model.buttonValid(1)
        self.view.setButtonText1(str(move))

    # Botão 2
    def clickField2(self):
        self.model.addPlayTable(0, 1)
        move = self.model.choosePlayer(2)
        self.model.buttonValid(2)
        self.view.setButtonText2(str(move))

    # Botão 3
    def clickField3(self):
        self.model.addPlayTable(0, 2)
        move = self.model.choosePlayer(3)
        self.model.buttonValid(3)
        self.view.setButtonText3(str(move))

    # Botão 4
    def clickField4(self):
        self.model.addPlayTable(1, 0)
        move = self.model.choosePlayer(4)
        self.model.buttonValid(4)
        self.view.setButtonText4(str(move))

    # Botão 5
    def clickField5(self):
        self.model.addPlayTable(1, 1)
        move = self.model.choosePlayer(5)
        self.model.buttonValid(5)
        self.view.setButtonText5(str(move))

    # Botão 6
    def clickField6(self):
        self.model.addPlayTable(1, 2)
        move = self.model.choosePlayer(6)
        self.model.buttonValid(6)
        self.view.setButtonText6(str(move))

    # Botão 7
    def clickField7(self):
        self.model.addPlayTable(2, 0)
        move = self.model.choosePlayer(7)
        self.model.buttonValid(7)
        self.view.setButtonText7(str(move))

    # Botão 8
    def clickField8(self):
        self.model.addPlayTable(2, 1)
        move = self.model.choosePlayer(8)
        self.model.buttonValid(8)
        self.view.setButtonText8(str(move))

    # Botão 9
    def clickField9(self):
        self.model.addPlayTable(2, 2)
        move = self.model.choosePlayer(9)
        self.model.buttonValid(9)
        self.view.setButtonText9(str(move))
