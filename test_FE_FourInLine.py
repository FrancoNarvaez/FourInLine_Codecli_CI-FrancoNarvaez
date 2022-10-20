#FrontEnd test_FourInLine

# import unittest

from test_FourInLine import FourInLine
from test_FourInLine import Overflow
from test_FourInLine import Winner
from test_FourInLine import OutOfRange
from test_FourInLine import NotNum
from test_FourInLine import Quit

class Frontendgame():
    def __init__(self):        
        self.game = FourInLine()
        self.combustible = True

    def tablero(self):
        for row in range(8):
            for column in range(8):
                print(" " + str(self.game.board[row][column]) + " ", end="")
            print("\n")

    def entrada(self):
        try:
            valor = int(input("Ingrese la columna (0-7): "))
            self.game.placeToken(valor)
        except Winner:
            print('You win')
            self.combustible = False
        except Overflow:
            print('Column full')
        except Quit:
            print("Vuelva pronto")
            self.combustible = False
        except OutOfRange:
            print('Numero fuera de rango, rango valido [0-7]')
        except NotNum:
            print("El valor ingresado no es un número")

    def motor(self):
        while self.combustible == True:
            self.tablero()
            self.entrada()
        
        self.tablero()

if __name__ == '__main__':
    jueguito = Frontendgame()
    jueguito.motor()
