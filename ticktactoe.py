#!/usr/bin/python3
## Request of user
## - Change coler when move - Done
# When user winer, have one line run left to right to congras this user with name 
#

import random
import os
import string
import time
import random
os.system('color')

X_SIGN = "X"
O_SIGN = "O"

class bcolors:
    OKBLUE = '\u001b[44;1m'
    OKGREEN = '\u001b[42;1m'
    OKRED = '\u001b[41;1m'
    ENDC = '\033[0m'

#Init table
TABLE_SIZE = 15
TABLE_MAX_SIZE = 24
NUMBER_WIN_SIGN = 5
UNDER_TABLE = string.ascii_lowercase
board = [ [ " " for i in range(TABLE_SIZE) ] for j in range(TABLE_SIZE) ] 

def drawBoard(board):
    print(end=" " * 2)
    for j in range(TABLE_SIZE):
        print("-+-", end=" ")
    print()
    for i in range(TABLE_SIZE):
        if (TABLE_SIZE - i < 10):
            print("0{0}".format(TABLE_SIZE - i), end=" ")
        else:
            print("{0}".format(TABLE_SIZE - i), end=" ")
        for j in range(TABLE_SIZE):
            if (board[i][j] != " "):
                if (board[i][j] == O_SIGN):
                    print("|" + bcolors.OKGREEN + " {0} ".format(board[i][j]) + bcolors.ENDC, end="")
                elif (board[i][j] == X_SIGN):
                    print("|" + bcolors.OKRED + " {0} ".format(board[i][j]) + bcolors.ENDC, end="")
            else:
                print("| {0} ".format(board[i][j]), end="")
        print()
        print(end=" " * 2)
        for j in range(TABLE_SIZE):
            print("-+-", end=" ")
        print()
    print(end=" " * 5) 
    for i in range(TABLE_SIZE):
        print(UNDER_TABLE[i], end= " " * 3)
    print()

class Player:
    name = ""
    position = ""
    signal = ""
    order = ""
    def __init__(self, name, signal, order):
        self.name = name
        self.signal = signal
        self.order = order

    def move(self):
        isOver = False
        print("{0} please move".format(self.name))
        coordinate = ""
        coordinate = input()
        isValid, x, y = checkValidMove(coordinate=coordinate, TABLE_SIZE=TABLE_SIZE, board=board)
        while not (isValid):
            print("Invalid move !!!. {0} please move again".format(self.name))
            coordinate = input()
            isValid, x, y = checkValidMove(coordinate=coordinate, TABLE_SIZE=TABLE_SIZE, board=board)
        board[x][y] = self.signal
        if (checkIsWin(board=board, x=x, y=y)):
            isOver = True
        #os.system('clear')
        drawBoard(board=board)
        return isOver
    def getPlayerName(self):
        print("Pleae enter your name")
        self.name = input().strip()
    def welcome(self):
        #self.getPlayerName()
        #self.getSignal()
        print("================================")
        print("Welcome {0}".format(self.name))
        print("Your signal is {0}".format(self.signal))
        print("You move first") if self.order == 0 else print("You move second")
        print("================================")
    def getSignal(self):
        signal = self.signal
        if (signal == ""):
            while not (signal == X_SIGN or signal == O_SIGN):
                print("You want {0} or {1}".format(X_SIGN, O_SIGN))
                signal = input().upper();
            self.signal = signal

def checkValidMove(coordinate, TABLE_SIZE, board):
    y = int(ord(coordinate[0]) - 97)
    x = int(coordinate[1:])
    if (x > TABLE_SIZE):
        return False, x, y
    isValid = True
    x = abs(TABLE_SIZE - x)
    if (x < 0 or x > TABLE_SIZE or y < 0 or y > TABLE_SIZE or board[x][y] != " "):
        isValid = False
    return isValid, x, y
def checkVerticalWin(board, x, y):
    count = 1
    CURRENT_SIGN = board[x][y]
    i = 1
    while (CURRENT_SIGN == board[x][y - i] and (y - i) > 0):
        count = count + 1
        i = i + 1
    j = 1
    while (CURRENT_SIGN == board[x][y + j] < TABLE_SIZE):
        count = count + 1
        j = j + 1
    print(count)
    if (count == NUMBER_WIN_SIGN and (board[x][y - i - 1] == " " or board[x][y + j + 1] == " ")):
        return True
    return False
            
def checkHorizonWin(board, x, y):
    count = 1
    CURRENT_SIGN = board[x][y]
    i = 1
    while (CURRENT_SIGN == board[x - i][y]):
        count = count + 1
        i = i + 1
    j = 1
    while (CURRENT_SIGN == board[x + j][y]):
        count = count + 1
        j = j + 1
    print(count)
    if (count == NUMBER_WIN_SIGN and (board[x - i - 1][y] == " " or board[x + j + 1][y] == " ")):
        return True
    return False
def checkMainDiagonalWin(board, x, y):
    count = 1
    CURRENT_SIGN = board[x][y]
    i = 1
    while (CURRENT_SIGN == board[x - i][y + i]):
        count = count + 1
        i = i + 1
    j = 1
    while (CURRENT_SIGN == board[x + j][y - j]):
        count = count + 1
        j = j + 1
    print(count)
    if (count == NUMBER_WIN_SIGN and (board[x - i - 1][y + i + 1] == " " or board[x + j + 1][y - j - 1] == " ")):
        return True
    return False
def checkAntiDiagonalWin(board, x, y):
    count = 1
    CURRENT_SIGN = board[x][y]
    i = 1
    while (CURRENT_SIGN == board[x - i][y - i]):
        count = count + 1
        i = i + 1
    j = 1
    while (CURRENT_SIGN == board[x + j][y + j]):
        count = count + 1
        j = j + 1
    print(count)
    if (count == NUMBER_WIN_SIGN and (board[x - i - 1][y - i - 1] == " " or board[x + j + 1][y + j + 1] == " ")):
        return True
    return False

def checkIsWin(board, x, y):
    if (checkHorizonWin(board=board, x=x, y=y) or 
        checkVerticalWin(board=board, x=x, y=y) or 
        checkMainDiagonalWin(board=board, x=x, y=y) or 
        checkAntiDiagonalWin(board=board, x=x, y=y)):
        return True
    return False
def printWinningMessage(message):
    i = 1
    while (True):
        for j in range(40):
            print("\t" * random.randint(0, 9), message)
        time.sleep(0.4)
        os.system('clear')
        i = i + 1

def gamePlay(board, player_1, player_2):
    isOver = False
    print("Welcome to the game, hope you have fun")
    drawBoard(board=board)
    while not (isOver):
        isOver = player_1.move()
        if (isOver):
            message = "Chuc mung {0} xinh dep tuyet voi ^^".format(player_1.name)
            printWinningMessage(message=message)

        isOver = player_2.move()
        if (isOver):
            message = "Chuc mung {0}".format(player_2.name)
            printWinningMessage(message=message)
    print("Game over !!!!")


if __name__ == "__main__":
    drawBoard(board=board)
    #Get player_1 info
    #player_1 = Player(0)
    #player_1.welcome()
    ##Get player_2 info
    #player_2 = Player(1)
    #if (player_1.signal == X_SIGN):
    #    player_2.signal = O_SIGN
    #else:
    #    player_2.signal == X_SIGN
    #player_2.welcome()
    player_1 = Player("Minh Thuy", "X", "0")
    player_2 = Player("Van Tu", "O", "1")
    gamePlay(board=board, player_1=player_1, player_2=player_2)



