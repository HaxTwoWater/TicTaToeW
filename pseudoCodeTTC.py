#On admet la function randint de la bibliotèque random qui retournera un nombre aléatoire entre x et y en prenant pour parametre x, y

#On initialise la liste grid avec pour index 0, 1 et 2 une liste de " ", " ", " "
#On initialise la liste symbols avec pour index 0 "X" et 1 "O"

#Definir la function displayGrid

    #Afficher grid d'index 0
    #Afficher grid d'index 1
    #Afficher grid d'index 2

#Definir la function checkWin de parametre move, player

    #On initialise check a 0

    #Pour i dans la liste grid d'index liste move d'index 0
        #Si i est égal a la liste symbols d'index player moins 1
            #Alors on incremente check d'un
    #Si check est égal a 3
        #Alors retourner Vraie

    #Pour i dans la liste grid
        #Si la liste i d'index liste move d'index 1 est égale a la liste symbols d'index player moins 1
            #Alors on incremente check d'un
    #Si check est égal a 3
        #Alors retourner Vraie

    #Si move est égal au parametre 0,0 ou que move est égal au parametre 1,1 ou que move est égal au parametre 2,2
        #Alors pour i dans le retour de l'execution de la fonction range de parametre 3
            #Si la liste grid d'index i et i est égal a la liste symbols d'index player moins 1
                #Alors on incremente check d'un
    #Si check est égal a 3
        #Alors retourner Vraie
    
    #Si move est égal au parametre 0, 2 ou que move est égal au parametre 1,1 ou que move est égal au parametre 2,0
        #Alors pour i dans le retour de l'execution de la fonction range de parametre 3
            #Si la liste grid d'index i et - (i + 1) est égal a la liste symbols d'index player moins 1
                #Alors on incremente check d'un
    #Si check est égal a 3
        #Alors retourner Vraie

    #Retourner Faux

#Definir la fonction intro
    #Afficher "Bienvenue dans le jeux du Morpion"
    #Tant que Vrai
        #On assigne a decision le retour de l'execution de la fonction input de parametre "Si vous voulez jouer a 2 joueur, ecrivez '2' dans la console, si vous voulez jouer contre les ia, ecrivez 'ia' dans la console"
        #Si decision est égal a "2"
            #Alors retour de l'execution de la fonction game
        #Si sinon decision est égal a "ai"
            #Alors
            #On assigne a decision2 le retour de l'execution de la fonction input de parametre  "Si vous voulez jouer contre le bot normal, ecrivez 'normal', si vous voulez jouer contre le bot impossible, ecrivez 'impossible'"
            #Si decision2 est égal a "normal"
                #Alors retour de l'execution de la fonction ai_morpion_random_game
            #Si sinon decision2 est égal a "impossible"
                #Alors retour de l'execution de la fonction ai_morpion_impossible_game
            #Sinon
                #Afficher "commande erronée"
        #Sinon
            #Afficher "commande erronée"


#Definir la fonction game

    #On intialise nbTour a 0

    #Tant que Vrai
        #Retour de l'execution de la fonction displayGrid
        #On assigne a player nbTour modulo 2 et additioné au tout 1
        #Si nbTour est égal a 9
            #Afficher "Egalité"
            #Break
        #Afficher "Joueur " + player " jouez"
        #On incremente nbTour d'un
        #On initialise correctMove a Faux
        #Tant que correctMove n'est pas Vrai
            #Essayer
                #On assigne a column la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la colonne : " moins 1
                #On assigne a ligne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la ligne : " moins 1
            #Exception
                #Afficher "Veuillez entrer des chiffres"
                #continue
            #Si column est inférieur ou égal a 2 et que column est supérieur ou égal a 0 et que line est inférieur ou égal a 2 et que line est supérieur ou égal a 0 et que la liste grid d'index line et column est égal a " "
                #Alors correctMove est égal a Vrai
            #Si sinon column est supérerieur a 2 ou que column est inférieur a 0 ou que line est supérieur a 2 ou que line est inférieur a 0
                #Alors afficher "la position sur la grille est invalide. Veuillez rerentrer la position"
            #Si sinon la liste grid d'index ligne et column n'est pas égal a " "
                #Alors afficher "la position sur la grille a déjà été joué. Veuillez rerentrer la position"
        #On assigne a grid d'index ligne et column la liste symbols d'index player moins 1
        #Afficher "Vous avez joué la case (" , column + 1, "," , line + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre line,column et player est égal a Vrai
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Joueur" , player , "à gagné. Merci d'avoir Jouer"
            #break
        
#Definir la fonction ai_morpion_random_game
    #On assigne a player_number le retour de l'execution de la fonction randint de parametre 0,1
    #On assigne a ai_player_number le retour de l'execution de la fonction abs de parametre player_number moins 1
    #Afficher "vous jouez les", symbols[player_number], "le bot joue les", symbols[ai_player_number]

    #On initialise nbTurn a 0

    #Definir ai_move
        #On initalise correctMove a Faux

        #Tant que correctMove n'est pas Vrai
            #On assigne a column le retour de l'execution de la fonction randint de parametre 0,2
            #On assigne a ligne le retour de l'execution de la fonction randint de parametre 0,2
            #Si la liste grid d'index line et column est égal a " "
                #Alors correctMove est égale a Vrai
        #On assigne a la liste grid d'index ligne et column la liste symbols d'index ai_player_number
        #Afficher "Le bot a joué la case (", column + 1, ",", line + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre line,column et ai_player_number+1 est égal a Vrai
            #Alors
            #Retour de l'execution de la fonction displayGrid
            #Retourner Vrai
        #Retourner Faux

    #Definir player_move
        #Afficher "veuillez jouer"
        #On initialise correctMove a Faux
        #Tant que correctMove n'est pas Vrai
            #Essayer
                #On assigne a column la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la colonne : " moins 1
                #On assigne a ligne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la ligne : " moins 1
            #Exception
                #Afficher "Veuillez entrer des chiffres"
                #continue
            #Si column est inférieur ou égal a 2 et que column est supérieur ou égal a 0 et que line est inférieur ou égal a 2 et que line est supérieur ou égal a 0 et que la liste grid d'index line et column est égal a " "
                #Alors correctMove est égal a Vrai
            #Si sinon column est supérerieur a 2 ou que column est inférieur a 0 ou que line est supérieur a 2 ou que line est inférieur a 0
                #Alors afficher "la position sur la grille est invalide. Veuillez rerentrer la position"
            #Si sinon la liste grid d'index ligne et column n'est pas égal a " "
                #Alors afficher "la position sur la grille a déjà été joué. Veuillez rerentrer la position"
        #On assigne a grid d'index ligne et column la liste symbols d'index player moins 1
        #Afficher "Vous avez joué la case (" , column + 1, "," , line + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre line,column et player est égal a Vrai
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Joueur" , player , "à gagné. Merci d'avoir Jouer"
            #Retourner Vrai
        #Retourner Faux
    
    #On assigne a nbTurn 0
    #Si player_numnber est égal a 1
        #Alors
        #Retour de l'execution de la fonction displayGrid
        #Retour de l'execution de la fonction ai_move
    
    #Tant que Vrai
        #Retour de l'execution de la fonction displayGrid
        #Si nbTurn est égal a 9
            #Alors
            #Afficher "Egalité"
            #break
        
        #Si player_move
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Vous avez gagner"
            #break
        #Si ai_move
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Vous avez perdue"
            #break


#Retour de l'execution de la fonction intro