import random

gameTabel = []

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
