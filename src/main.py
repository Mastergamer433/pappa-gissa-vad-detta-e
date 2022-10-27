"""This is the main file for this game."""

import numpy as np


class GameData:
    """This is where all the data for the game is store,
       such as board, turn and so on and so forth."""
    multiplayer = False
    boardSize = 9
    board = []
    turn = "X"
    # def __init__():


gameData = GameData()


def initGame():
    """Init fuction for initializing all variables."""
    i = 0
    while i != (gameData.boardSize * gameData.boardSize):
        gameData.board.append("-")
        i += 1


def startGame():
    """Start function for starting the game."""
    if gameData.multiplayer is True:
        while True:
            print("multiplayer")
            printBoard()
            move()
            checkWin()
            switchTurn()
    else:
        while True:
            printBoard()
            if gameData.turn == "O":
                computerMove()
            else:
                move()
            checkWin()
            switchTurn()


def printBoard():
    """Print board fuction for printing out the board every turn"""
    i = 0
    while i < gameData.boardSize:
        if i == 3 or i == 6 or i == 9:
            print("\n", end='')
        print(gameData.board[i], end='')
        i += 1
    print("\n")


def move():
    """Move function for doing a move"""
    invalidMove = True
    while invalidMove is True:
        Move = input(gameData.turn + " it is your turn (1-9): ")
        Move = int(Move)
        if gameData.board[Move-1] == "-":
            invalidMove = False
            gameData.board[Move-1] = gameData.turn
        else:
            print(
                "That move is impossible because \
the other player is occupying that spot."
            )


def computerMove():
    """Computer move function for when the computer should make a move"""
    invalidMove = False
    while invalidMove:
        Move = np.random(1, gameData.boardSize)
        if gameData.board[Move-1] == "-":
            gameData.board[Move-1] == gameData.turn


def checkWin():
    if gameData.board[0] == gameData.turn and\
    gameData.board[1] == gameData.turn and\
    gameData.board[2] == gameData.turn or\
    gameData.board[0] == gameData.turn and\
    gameData.board[4] == gameData.turn and\
    gameData.board[8] == gameData.turn or\
    gameData.board[2] == gameData.turn and\
    gameData.board[4] == gameData.turn and\
    gameData.board[6] == gameData.turn or\
    gameData.board[0] == gameData.turn and\
    gameData.board[3] == gameData.turn and\
    gameData.board[6] == gameData.turn or\
    gameData.board[1] == gameData.turn and\
    gameData.board[4] == gameData.turn and\
    gameData.board[7] == gameData.turn or\
    gameData.board[2] == gameData.turn and\
    gameData.board[5] == gameData.turn and\
    gameData.board[8] == gameData.turn or\
    gameData.board[3] == gameData.turn and\
    gameData.board[4] == gameData.turn and\
    gameData.board[5] == gameData.turn or\
    gameData.board[6] == gameData.turn and\
    gameData.board[7] == gameData.turn and\
    gameData.board[8] == gameData.turn:
        print(gameData.turn + " won!")
        exit(0)


def switchTurn():
    """Switch turn function to switch turn"""
    if gameData.turn == "X":
        gameData.turn = "O"
    else:
        gameData.turn = "X"


def main():
    """Entry function, its where everything begins."""
    mp = input(
        "Do you wanna play against another player or the computer? (Y/n) "
    )
    if(mp == "n"):
        gameData.multiplayer = False
    else:
        gameData.multiplayer = True
    initGame()
    startGame()


main()
