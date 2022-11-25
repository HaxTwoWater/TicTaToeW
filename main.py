from random import randint, choice
import webbrowser


symbols = ("X", "O")
global ai_played_move
ai_played_move=[]

def displayGrid():
    print(grid[0])
    print(grid[1])
    print(grid[2])

def checkwin(move, player):
    check = 0

    for i in grid[move[0]]:
        if i == symbols[player - 1]:
            check += 1

    if check == 3:
        return True

    check = 0

    for i in grid:
        if i[move[1]] == symbols[player - 1]:
            check += 1

    if check == 3:
        return True

    check = 0

    if move == (0, 0) or move == (1, 1) or move == (2, 2):
        for i in range(3):
            if grid[i][i] == symbols[player - 1]:
                check += 1

    if check == 3:
        return True

    check = 0

    if move == (0, 2) or move == (1, 1) or move == (2, 0):
        for i in range(3):
            if grid[i][-(i + 1)] == symbols[player - 1]:
                check += 1

    if check == 3:
        return True

    return False


def intro():
    lose_streak = 0
    print("Bienvenue dans le jeux du Morpion")
    global grid
    global ai_played_move
    while True:
        grid = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]] #reinitialiser le tableau a chaque début de partie
        ai_played_move = [] #reinitialise la liste
        decision = input(
            "Si vous voulez jouer a 2 joueur, ecrivez '2' dans la console, si vous voulez jouer contre les ia, ecrivez 'ia' dans la console, si vous voulez arreter de jouer, ecrivez 'stop' dans la console")
        if decision == "2":
            game()
        elif decision == "ai":
            decision2 = input(
                "Si vous voulez jouer contre le bot normal, ecrivez 'normal', si vous voulez jouer contre le bot impossible, ecrivez 'impossible'")
            if decision2 == "normal":
                if ai_morpion_random_game():
                    lose_streak+=1
            elif decision2 == "impossible":
                if ai_morpion_impossible_game():
                    lose_streak+=1
            else:
                print("commande erronée")
        elif decision == "stop":
            break
        else:
            print("commande erronnée")
        if lose_streak == 3:
            webbrowser.open('https://www.youtube.com/watch?v=vfc42Pb5RA8')
            print("Vous êtes nuls retournez sur pokemon, vosu avez perdue 3 fois d'affilé")


def game():
    print("Pour chaque tours vous rentrerez le numero de la colonne que vous voulez remplir puis le numero de la ligne")
    nbTour = 0

    while True:

        displayGrid()
        player = (nbTour % 2) + 1

        if nbTour == 9:
            print("Egalité")
            break

        print("Joueur ", player, "jouez")
        nbTour += 1
        correctmove = False

        while not correctmove:

            try:

                colonne = int(input("Entrez le numero de la colonne : ")) - 1
                ligne = int(input("Entrez le numero de la ligne : ")) - 1
            except:

                print("veuillez entrer des chiffres")
                continue

            if colonne <= 2 and colonne >= 0 and ligne <= 2 and ligne >= 0 and grid[ligne][colonne] == " ":
                correctmove = True

            elif colonne > 2 or colonne < 0 or ligne > 2 or ligne < 0:
                print("la position sur la grille est invalide. Veuillez rerentrer la position")

            elif grid[ligne][colonne] != " ":
                print("la position sur la grille a déjà été joué. Veuillez rerentrer la position")

        grid[ligne][colonne] = symbols[player - 1]
        print("Vous avez joué la case (", colonne + 1, ",", ligne + 1, ")")

        if checkwin((ligne, colonne), player) == True:
            displayGrid()
            print("Joueur", player, "à gagné. Merci d'avoir Jouer")
            break

def ai_random_move(ai_player_number):
    correctmove = False

    while not correctmove:
        colonne = randint(0, 2)
        ligne = randint(0, 2)
        if grid[ligne][colonne] == " ":
            correctmove = True
    grid[ligne][colonne] = symbols[ai_player_number]
    print("Le bot a joué la case (", colonne + 1, ",", ligne + 1, ")")
    if checkwin((ligne, colonne), ai_player_number + 1) == True:
        displayGrid()
        return True
    return False

def player_move(player_number):
    print("veuillez jouer")

    correctmove = False

    while not correctmove:

        try:

            colonne = int(input("Entrez le numero de la colonne : ")) - 1
            ligne = int(input("Entrez le numero de la ligne : ")) - 1
        except:

            print("veuillez entrer des chiffres")
            continue

        if colonne <= 2 and colonne >= 0 and ligne <= 2 and ligne >= 0 and grid[ligne][colonne] == " ":
            correctmove = True

        elif colonne > 2 or colonne < 0 or ligne > 2 or ligne < 0:
            print("la position sur la grille est invalide. Veuillez rerentrer la position")

        elif grid[ligne][colonne] != " ":
            print("la position sur la grille a déjà été joué. Veuillez rerentrer la position")

    grid[ligne][colonne] = symbols[player_number]
    print("Vous avez joué la case (", colonne + 1, ",", ligne + 1, ")")

    if checkwin((ligne, colonne), player_number + 1) == True:
        displayGrid()
        print("Joueur", player_number + 1, "à gagné. Merci d'avoir Jouer")
        return True
    return False

def ai_morpion_random_game():
    player_number = randint(0, 1)
    ai_player_number = abs(player_number - 1)
    print("vous jouez les", symbols[player_number], "le bot joue les", symbols[ai_player_number])
    nbTour = 0
    if player_number == 1:
        displayGrid()
        ai_random_move(ai_player_number)
        nbTour+=1

    while True:
        displayGrid()
        if nbTour == 9:
            print("Egalité")
            break

        if player_move(player_number):
            displayGrid()
            print("vous avez gagner")
            break
        nbTour += 1
        if nbTour == 9:
            displayGrid()
            print("Egalité")
            break
        if ai_random_move(ai_player_number):
            displayGrid()
            print("vous avez perdu")
            break
        nbTour += 1

def check_symbol(move):
    return grid[move[0]][move[1]]

def ai_impossible_move(ai_player_number,nbTour,ai_played_move):
    moved_choice = False
    if nbTour==0:
        move = choice(((0,0),(2,2),(0,2),(2,0)))
        colonne = move[1]
        ligne = move[0]
        ai_played_move.append((ligne,colonne))
        moved_choice = True
    else:

        for i in range(3):
            for j in range(3):
                if grid[i][j] == " ":
                    grid[i][j] = symbols[ai_player_number]
                    if checkwin((i, j), ai_player_number+1):
                        ligne = i
                        colonne = j
                        moved_choice = True
                        ai_played_move.append((ligne, colonne))
                    grid[i][j] = " "
        if not moved_choice:
            for i in range(3):
                for j in range(3):
                    if grid[i][j] == " ":
                        grid[i][j] = symbols[abs(ai_player_number - 1)]
                        if checkwin((i, j), (abs(ai_player_number - 1)+1)):
                            ligne = i
                            colonne = j
                            moved_choice = True
                            ai_played_move.append((ligne, colonne))
                        grid[i][j] = " "

        if not moved_choice:
            if nbTour == 2 and check_symbol((1,1)) == symbols[abs(ai_player_number-1)]:
                if ai_played_move[0][1]==0:
                    colonne = 2
                elif ai_played_move[0][1]==2:
                    colonne = 0
                if ai_played_move[0][0] == 0:
                    ligne = 2
                elif ai_played_move[0][0] == 2:
                    ligne = 0
                moved_choice = True
                ai_played_move.append((ligne, colonne))
            elif nbTour == 2 and check_symbol((1,1)) == " ":
                for i in range(3):
                    for j in range(3):
                        if check_symbol((i,j)) == symbols[abs(ai_player_number-1)]:
                            for k,l in ((0,0),(0,2),(2,0),(2,2)):
                                if check_symbol((k,l)) == " " and (k != i and l!= j) and (k == ai_played_move[0][0] or l == ai_played_move[0][1]):
                                    ligne = k
                                    colonne= l
                                    moved_choice = True
                                    ai_played_move.append((ligne, colonne))
            elif nbTour == 4:
                enemy_middle_position = 0
                for i, j in ((0,1),(1,0),(2,1),(1,2)):
                    if check_symbol((i,j)) == symbols[abs(ai_player_number-1)]:
                        enemy_middle_position +=1
                if enemy_middle_position == 2:
                    ligne = 1
                    colonne = 1
                    moved_choice = True
                    ai_played_move.append((ligne,colonne))
                else:
                    for k, l in ((0, 0), (0, 2), (2, 0), (2, 2)):
                        if check_symbol((k,l))==" ":
                            ligne = k
                            colonne = l
                            moved_choice = True
                            ai_played_move.append((ligne, colonne))

            elif nbTour==1:
                if check_symbol((1,1)) == symbols[abs(ai_player_number-1)]:
                    move = choice(((0, 0), (2, 2), (0, 2), (2, 0)))
                    colonne = move[1]
                    ligne = move[0]
                    ai_played_move.append((ligne, colonne))
                    moved_choice = True
                else:
                    ligne = 1
                    colonne = 1
                    ai_played_move.append((ligne, colonne))
                    moved_choice = True
            elif nbTour == 3:
                enemy_middle_position = []
                for i, j in ((0,1),(1,0),(2,1),(1,2)):
                        if check_symbol((i,j)) == symbols[abs(ai_player_number-1)]:
                            enemy_middle_position.append([i,j])
                if len(enemy_middle_position) == 2:
                    if enemy_middle_position[0][0]==enemy_middle_position[1][0] or enemy_middle_position[0][1]==enemy_middle_position[1][1]:
                        move = choice(((0, 0), (2, 2), (0, 2), (2, 0)))
                        colonne = move[1]
                        ligne = move[0]
                        ai_played_move.append((ligne, colonne))
                        moved_choice = True
                    else:
                        for i,j in ((0, 0), (0, 2), (2, 0), (2, 2)):
                            if (i == enemy_middle_position[0][0] and j == enemy_middle_position[1][1]) or (i == enemy_middle_position[1][0] and j == enemy_middle_position[0][1]):
                                ligne = i
                                colonne = j
                                moved_choice = True
                                ai_played_move.append((ligne, colonne))
                elif len(enemy_middle_position)==0:
                    move = choice(((0, 1), (1, 0), (2, 1), (1, 2)))
                    colonne = move[1]
                    ligne = move[0]
                    ai_played_move.append((ligne, colonne))
                    moved_choice = True
                else:
                    enemy_corner_position = []
                    for i,j in ((0, 0), (0, 2), (2, 0), (2, 2)):
                        if check_symbol((i,j)) == symbols[abs(ai_player_number-1)]:
                            enemy_corner_position.append([i,j])
                        elif enemy_middle_position[0][0]==1:
                            colonne =enemy_middle_position [0],[1]
                            ligne = enemy_corner_position[0][0]
                            ai_played_move.append((ligne, colonne))
                            moved_choice = True
                        elif enemy_middle_position[0][1]==1:

                            colonne = enemy_corner_position[0][1]
                            ligne = enemy_middle_position [0],[0]
                            ai_played_move.append((ligne, colonne))
                            moved_choice = True
            elif nbTour == 5:
                possible_move = []
                for i,j in ((0, 0), (0, 2), (2, 0), (2, 2)):
                    if check_symbol((i, j)) == " ":
                        possible_move.append([i, j])
                move = choice(possible_move)
                colonne = move[1]
                ligne = move[0]
                ai_played_move.append((ligne, colonne))
                moved_choice = True
            elif nbTour == 7:
                possible_move = []
                for i in range(3):
                    for j in range(3):
                        if check_symbol((i,j)) == " ":
                            possible_move.append((i,j))
                move = choice(possible_move)
                colonne = move[1]
                ligne = move[0]
                ai_played_move.append((ligne, colonne))
                moved_choice = True

    if moved_choice:
        grid[ligne][colonne] = symbols[ai_player_number]
    print("Le bot a joué la case (", colonne + 1, ",", ligne + 1, ")")
    if checkwin((ligne, colonne), ai_player_number + 1) == True:
        displayGrid()
        return True
    return False

def ai_morpion_impossible_game():
    player_number = randint(0, 1)
    ai_player_number = abs(player_number - 1)
    print("vous jouez les", symbols[player_number], "le bot joue les", symbols[ai_player_number])

    nbTour = 0
    if player_number == 1:
        displayGrid()
        ai_impossible_move(ai_player_number,nbTour,ai_played_move)
        nbTour += 1
    while True:
        displayGrid()
        if nbTour == 9:
            print("Egalité")
            return

        if player_move(player_number):
            displayGrid()
            print("vous avez gagner")
            return
        nbTour += 1
        if nbTour == 9:
            displayGrid()
            print("Egalité")
            break
        if ai_impossible_move(ai_player_number,nbTour,ai_played_move):
            displayGrid()
            print("vous avez perdu")
            return True
        nbTour += 1



intro()


