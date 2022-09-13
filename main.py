from view import View
from controller import Controller
from velha import Velha

view = View(Controller)
velha = Velha()
# Passando os argumentos necessarios pro controller
controller = Controller(view, velha)

view.setController(controller)  # Setano o controller na view

view.run()  # Inicializando o run
