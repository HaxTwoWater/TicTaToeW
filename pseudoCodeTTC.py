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
                #On assigne a colonne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la colonne : " moins 1
                #On assigne a ligne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la ligne : " moins 1
            #Exception
                #Afficher "Veuillez entrer des chiffres"
                #continue
            #Si colonne est inférieur ou égal a 2 et que colonne est supérieur ou égal a 0 et que ligne est inférieur ou égal a 2 et que ligne est supérieur ou égal a 0 et que la liste grid d'index ligne et colonne est égal a " "
                #Alors correctMove est égal a Vrai
            #Si sinon colonne est supérerieur a 2 ou que colonne est inférieur a 0 ou que ligne est supérieur a 2 ou que ligne est inférieur a 0
                #Alors afficher "la position sur la grille est invalide. Veuillez rerentrer la position"
            #Si sinon la liste grid d'index ligne et colonne n'est pas égal a " "
                #Alors afficher "la position sur la grille a déjà été joué. Veuillez rerentrer la position"
        #On assigne a grid d'index ligne et colonne la liste symbols d'index player moins 1
        #Afficher "Vous avez joué la case (" , colonne + 1, "," , ligne + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre ligne,colonne et player est égal a Vrai
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Joueur" , player , "à gagné. Merci d'avoir Jouer"
            #break
        
#Definir la fonction ai_morpion_random_game
    #On assigne a player_number le retour de l'execution de la fonction randint de parametre 0,1
    #On assigne a ai_player_number le retour de l'execution de la fonction abs de parametre player_number moins 1
    #Afficher "vous jouez les", symbols[player_number], "le bot joue les", symbols[ai_player_number]

    #On initialise nbTour a 0

    #Definir ai_move
        #On initalise correctMove a Faux

        #Tant que correctMove n'est pas Vrai
            #On assigne a colonne le retour de l'execution de la fonction randint de parametre 0,2
            #On assigne a ligne le retour de l'execution de la fonction randint de parametre 0,2
            #Si la liste grid d'index ligne et colonne est égal a " "
                #Alors correctMove est égale a Vrai
        #On assigne a la liste grid d'index ligne et colonne la liste symbols d'index ai_player_number
        #Afficher "Le bot a joué la case (", colonne + 1, ",", ligne + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre ligne,colonne et ai_player_number+1 est égal a Vrai
            #Alors
            #Retour de l'execution de la fonction displayGrid
            #Retourner Vrai
        #Retourner Faux

    #Definir player_move
        #Afficher "veuillez jouer"
        #On initialise correctMove a Faux
        #Tant que correctMove n'est pas Vrai
            #Essayer
                #On assigne a colonne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la colonne : " moins 1
                #On assigne a ligne la convertion en integer le retour de l'execution de la fonction input de parametre "Entrez le numero de la ligne : " moins 1
            #Exception
                #Afficher "Veuillez entrer des chiffres"
                #continue
            #Si colonne est inférieur ou égal a 2 et que colonne est supérieur ou égal a 0 et que ligne est inférieur ou égal a 2 et que ligne est supérieur ou égal a 0 et que la liste grid d'index ligne et colonne est égal a " "
                #Alors correctMove est égal a Vrai
            #Si sinon colonne est supérerieur a 2 ou que colonne est inférieur a 0 ou que ligne est supérieur a 2 ou que ligne est inférieur a 0
                #Alors afficher "la position sur la grille est invalide. Veuillez rerentrer la position"
            #Si sinon la liste grid d'index ligne et colonne n'est pas égal a " "
                #Alors afficher "la position sur la grille a déjà été joué. Veuillez rerentrer la position"
        #On assigne a grid d'index ligne et colonne la liste symbols d'index player moins 1
        #Afficher "Vous avez joué la case (" , colonne + 1, "," , ligne + 1, ")"
        #Si le retour de l'execution de la fonction checkWin de parametre ligne,colonne et player est égal a Vrai
            #Retour de l'execution de la fonction displayGrid
            #Afficher "Joueur" , player , "à gagné. Merci d'avoir Jouer"
            #Retourner VraiAlors
        #Retourner Faux
    
    #On assigne a nbTour 0
    #Si player_numnber est égal a 1
        #Alors
        #Retour de l'execution de la fonction displayGrid
        #Retour de l'execution de la fonction ai_move
    
    #Tant que Vrai
        #Retour de l'execution de la fonction displayGrid
        #Si nbTour est égal a 9
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

#Definir ai_impossible_move de parametre ai_player_number,nbTour,ai_played_move
    #On initialise moved_choice a Faux
    #Si nbTour est égal a 0
        #Alors
        #On assigne a move choice de parametre ((0,0),(2,2),(0,2),(2,0))
        #On assigne a colonne la liste move d'index 1
        #On assigne a ligne la liste move d'index 0
        #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
        #On assigne a moved_choice Vrai
    #Sinon
        #Pour i dans le retour de l'execution de la fonction range de parametre 3
            #Pour j dans le retour de l'execution de la fonction range de parametre 3
                #Si grid d'index i et j est égal a " "
                    #Alors on assigne a la liste grid d'index i et j la liste symbols d'index ai_player_number
                    #Si le retour de l'exectuion de la fonction checkWin de parametre (i,j) et ai_player_number plus 1
                        #Alors
                        #On assigne a ligne i
                        #On assigne a colonne j
                        #On assigne a moved_choice Vrai
                        #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
                    #On assigne a la liste grid d'index i et j " "
        #Si moved_choice n'est pas Vrai
            #Alors pour i dans le retour de l'execution de la fonction range de parametre 3
                #Pour j dans le retour de l'execution de la fonction range de parametre 3
                    #Si la liste grid d'index i et j est égal a " "
                        #Alors on assigne a grid d'index i et j la liste symbols d'index du retour de l'execution de la fonction abs de parametre ai_player_number moins 1
                        #Si le retour de l'execution de la fonction checkwin de parametre (i,j) et du retour de l'execution de la fonction abs de parametre ai_player_number moins 1 le tout additioné de  1
                            #Alors
                            #On assigne a ligne i
                            #On assigne a colonne j
                            #On assigne a moved_choice Vrai
                            #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
                        #On assigne a la liste grid d'index i et j " "
        #Si moved_choice n'est pas Vrai
            #Alors 
            #Si nbTour est égal a 2 et que le retour de l'execution de la fonction check_symbol de parametre (1,1) est égal a la liste symbols d'index du retour de l'execution de la fonction abs de parametre ai_player_number moins 1
                #Alors
                #Si la liste ai_played_move d'index 0 et 1 est égal a 0
                    #Alors on assigne a colonne 2
                #Si sinon la liste ai_played_move d'index 0 et 1 est égal a 2
                    #Alors on assigne colonne 0
                #Si la liste ai_played_move d'index 0 et 0 est égal a 0
                    #Alors on assigne a ligne 2
                #Si sinon la liste ai_played_move d'index 0 et 0 est égal a 2
                    #Alors on assigne a ligne 0
                #On asigne a moved_choice Vrai
                #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
            #Si sinon nbTour est égal a 2 et que le retour de l'execution de la fonction check_symbol de parametre (1,1) est égal a " "
                #Alors pour i dans le retour de l'execution de la fonction range de parametre 3
                    #Pour j dans le retour de l'execution de la fonction range de parametre 3
                        #Si le retour de l'execution de la fonction check_symbol de parametre (i,j) est égal a la liste symbols d'index du retour de l'execution de la fonction abs de parametre ai_player_number moins 1
                            #Alors
                            #Pour k et l dans ((0,0),(0,2),(2,0),(2,2))
                                #Si le retour de l'execution de la fonction check_symbol de parametre (k,l) est égal a " " et que k n'est pas égal a i est que  l n'est pas égal a j et que k est égal la liste ai_played_move d'index 0 et 0 our que l est égal a la liste ai_played_move d'index O et 1
                                    #Alors
                                    #On assigne a ligne k
                                    #On assigne a colonne l
                                    #On assigne a moved_choice Vrai
                                    #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
            #Si sinon nbTour est égal a 4
                #Alors
                #On assigne a enemy_middle_position 0
                #Pour i et j dans ((0,1),(1,0),(2,1),(1,2))
                    #Si le retour de l'execution de la fonction check_symbol de parametre (i,j) est égal a la liste symbols d'index du rtour de l'execution de la fonction abs de parametre ai_player_number moins 1
                        #Alors on incremente enemy_middle_position d'un
                #Si enemy_middle_position est égal a 2
                    #Alors
                    #On assigne a ligne 1
                    #On assigne a colonne 1
                    #On assigne a moved_choice Vrai
                    #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
                #Sinon
                    #Pour k et l dans ((0, 0), (0, 2), (2, 0), (2, 2))
                        #Si le retour de l'execution de la fonction check_symbol de parametre (k,l) est égal a " "
                            #On assigne a ligne k
                            #On assigne a colonne l
                            #On assigne a moved_choice Vrai
                            #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
            #Si sinon nbTour est égal a 1
                #Alors
                #Si le retour de l'execution de la fonction check_symbol de parametre (1,1) est égal a la liste symbols d'index du retour de l'execution de la fonction abs de parametre ai_player_number moins 1
                    #Alors
                    #On assigne a move le retour de l'execution de la fonction choice de parametre ((0, 0), (2, 2), (0, 2), (2, 0))
                    #On assigne a colonne la liste move d'index 1
                    #On assigne a ligne la liste move d'index 0
                    #On assigne a moved_choice Vrai
                    #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
            #Si sinon nbTour est égal a 3
                #Alors
                #On initialise la liste enemy_middle_position 
                #Pour i et j dans ((0,1),(1,0),(2,1),(1,2))
                    #Si le retour de l'execution de la fonction check_symbol de parametre (i,j) est égal a la liste symbols d'index du retour de l'execution de la fonction abs de parametre ai_player_number moins 1
                        #Alors
                        #enemy_middle_position.append([i,j])
                #Si le retour de l'execution de la fonction len de parametre enemy_middle_position est égal a 2
                    #Alors
                    #Si la liste enemy_middle_position d'index 0 et 0 est égal a la liste enemy_middle_position d'index 1 et 0 ou que la liste d'index 0 et 1 est égal a la liste enemy_middle_position d'index 1 et 1
                        #Alors
                        #On assigne a le retour de l'execution de la fonction choice de parametre ((0, 0), (2, 2), (0, 2), (2, 0))
                        #On assigne a colonne la liste move d'index 1
                        #On assigne a ligne la lite move d'index 0
                        #On assigne a moved_choice Vrai
                        #Retour de l'execution de la fonction ai_played_move de parammetre .append((ligne,colonne))
                    #Sinon
                        #Pour i et j dans ((0, 0), (0, 2), (2, 0), (2, 2))            


#Retour de l'execution de la fonction intro