import random

gameTable = []
gameTable.append("-", "-", "-")
gameTable.append("-", "-", "-")
gameTable.append("-", "-", "-")

numberTable = []
numberTable.append("1", "2", "3")
numberTable.append("4", "5", "6")
numberTable.append("7", "8", "9")

def gameIntro():
    print("Welcome to our TicTaToe !")
    modeAsking = input("Against who you want to play ? (IA or Player)").lower()
    if modeAsking == "ai":
        diffAsking = input("Wich difficulty you want the IA to be ? (Impossible or Normal)").lower()
        if diffAsking == "impossible" or diffAsking == "i":
            iaDiffImp()
        elif diffAsking == "normal" or diffAsking == "n":
            iaDiffNor()
        else:
            print("Wrong Value")
            gameIntro()
    elif modeAsking == "player":
        playerMode()
    else:
        print("Wrong Value")
        gameIntro()
    
def game():

    for i in range(0):
        print("")

def iaDiffImp():
    #Premier tour
    print("t")

def iaDiffNor():
    print("lorem")

def playerMode():
    print("")