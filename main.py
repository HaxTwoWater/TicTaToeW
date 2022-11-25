#Initialization of the grid and the symbols for the player
grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
symbols = ("X","O")

#Function to print the grid
def displayGrid():

    print(grid[0])
    print(grid[1])
    print(grid[2])

#Function to check if the actual player is winning or not
def checkWin(move, player):

    check = 0
    #Check for the horizontal win
    for i in grid[move[0]]:
        if i == symbols[player-1]:
            check +=1
    if check == 3:
        return True
    check = 0
    #Vertical one
    for i in grid:
        if i[move[1]] == symbols[player-1]:
            check+=1
    if check == 3:
        return True
    check = 0
    #And the two diagonals
    if move == (0,0) or move == (1,1) or move == (2,2):
        for i in range(3):
            if grid[i][i] == symbols[player-1]:
                check+=1
    if check == 3:
        return True
    check = 0
    if move == (0,2) or move == (1,1) or move == (2,0):
        for i in range(3):
            if grid[i][-(i+1)] == symbols[player-1]:
                check+=1
    if check == 3:
        return True
    return False #Neither of check returned True return false to continue playing

def intro():
    print("Bienvenue dans le jeux du Morpion")
    while True:
        decision = input("Si vous voulez jouer a 2 joueur, ecrivez '2' dans la console, si vous voulez jouer contre les ia, ecrivez 'ia' dans la console")
        if decision == "2":
            game()
        elif decision == "ai":
            decision2 = input("Si vous voulez jouer contre le bot normal, ecrivez 'normal', si vous voulez jouer contre le bot impossible, ecrivez 'impossible'")
            if decision2 == "normal":
                ai_morpion_random_game()
            elif decision2 == "impossible":
                ai_morpion_impossible_game()
            else:
                print("commande erronée")
        else:
            print("commande erronnée")

#Function of the game
def game():

    nbTurn = 0

    #While true the game is playing
    while True:
        displayGrid() #printing the grid
        player = (nbTurn%2)+1 #decide which player is playing
        if nbTurn == 9:
            print("Egalité")
            break
        print("Joueur ", player, "jouez")
        nbTurn += 1
        correctMove = False
        while not correctMove: #while the correctMove isn't true asking for the position of the move
            try:
                column = int(input("Entrez le numero de la colonne : "))-1
                line = int(input("Entrez le numero de la ligne : "))-1
            except:
                print("veuillez entrer des chiffres")
                continue
            if column <= 2 and column>= 0 and  line <= 2 and line >=0 and grid[line][column] == " ":
                correctMove = True
            elif column > 2 or column < 0 or line > 2 or line < 0:
                print("la position sur la grille est invalide. Veuillez rerentrer la position")
            elif grid[line][column] != " ":
                print("la position sur la grille a déjà été joué. Veuillez rerentrer la position")
        grid[line][column] = symbols[player-1]
        print("Vous avez joué la case (" , column + 1, "," , line + 1, ")")
        if checkWin((line,column), player) == True:
            displayGrid()
            print("Joueur" , player , "à gagné. Merci d'avoir Jouer")
            break

def ai_morpion_random_game():
    player_number = randint(0,1)
    ai_player_number = abs(player_number-1)
    print("vous jouez les", symbols[player_number], "le bot joue les", symbols[ai_player_number])

    nbTurn = 0
    def ai_move():
        correctMove = False

        while not correctMove:
            column = randint(0,2)
            line = randint(0,2)
            if grid[line][column] == " ":
                correctMove = True
        grid[line][column] = symbols[ai_player_number]
        print("Le bot a joué la case (", column + 1, ",", line + 1, ")")
        if checkWin((line, column), ai_player_number+1) == True:
            displayGrid()
            return True
        return False
    def player_move():
        print("veuillez jouer")

        correctMove = False

        while not correctMove:
            try:
                column = int(input("Entrez le numero de la colonne : ")) - 1
                line = int(input("Entrez le numero de la ligne : ")) - 1
            except:

                print("veuillez entrer des chiffres")
                continue

            if column <= 2 and column >= 0 and line <= 2 and line >= 0 and grid[line][column] == " ":
                correctMove = True

            elif column > 2 or column < 0 or line > 2 or line < 0:
                print("la position sur la grille est invalide. Veuillez rerentrer la position")

            elif grid[line][column] != " ":
                print("la position sur la grille a déjà été joué. Veuillez rerentrer la position")

        grid[line][column] = symbols[player_number]
        print("Vous avez joué la case (", column + 1, ",", line + 1, ")")

        if checkWin((line, column), player_number+1) == True:
            displayGrid()
            print("Joueur", player_number + 1, "à gagné. Merci d'avoir Jouer")
            return True
        return False

    nbTurn = 0
    if player_number == 1:
        displayGrid()
        ai_move()

    while True:
        displayGrid()
        if nbTurn == 9:
            print("Egalité")
            break

        if player_move():
            displayGrid()
            print("vous avez gagner")
            break
        if ai_move():
            displayGrid()
            print("vous avez perdu")
            break

intro()