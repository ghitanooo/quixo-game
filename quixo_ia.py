"""Fichier Quixo_ia

Classe:
    * QuixoIA - Classe utilisée pour jouer automatiquement contre l'ordinateur
"""
import random

from quixo import Quixo

from quixo_error import QuixoError

class QuixoIA(Quixo):
    """
    Fonctions:
        * lister_les_coups_possibles
        * analyser_le_plateau
        * partie_terminée
        * trouver_un_coup_vainqueur
        * trouver_un_coup_bloquant
        * jouer_un_coup
    """
    def lister_les_coups_possibles(self, plateau, cube):
        """Lister tous les coups possibles dans une partie

        Args: 
            * Un plateau de jeu
            * Symbole du cube représentant le joueur

        Return:
            *Liste de dictionnaires des coups possibles pour le joueur spécifié

        Raise: 
            *QuixoError si le cube n'est pas valide, ou si la parties est terminée
        """
        if cube not in ('X', 'O'):
            raise QuixoError('Le cube doit être "X" ou "O".')
        if self.partie_terminée() is not None:
            raise QuixoError('La partie est déjà terminée.')
        coups_possibles = []
        for x in range(5):
            for y in range (5):
                if (x in [0, 4] or (
                    y in [0, 4]) and (
                        plateau[x][y] in [cube, ' '])):
                    if x != 0:
                        coups_possibles.append({'origine': [y+1, x+1], 'direction': 'haut'})
                    if x != 4:
                        coups_possibles.append({'origine': [y+1, x+1], 'direction': 'bas'})
                    if y != 0:
                        coups_possibles.append({'origine': [y+1, x+1], 'direction': 'gauche'})
                    if y != 4:
                        coups_possibles.append({'origine': [y+1, x+1], 'direction': 'droite'})
        return coups_possibles


    def analyser_le_plateau(self, plateau):
        """ Liste pour chaque joueur, le nombre de lignes de 2,3,4 et 5 cubes qu'il possède
        Args: 
            *plateau

        Return:
            *Dictionnaire contenant les clés 'X' et 'O' associées à un dictionnaire
            *Dictionnaire possédant les clés (2,3,4,5),
            associées au nombre de lignes du nombre de cubes
            """
        resultat = {
            "X": {"2": 0, "3": 0, "4": 0, "5": 0},
            "O": {"2": 0, "3": 0, "4": 0, "5": 0}
        }

        for ligne in plateau:
            if ligne.count("X") > 1:
                resultat["X"][str(ligne.count("X"))] += 1
            if ligne.count("O") > 1:
                resultat["O"][str(ligne.count("O"))] += 1

        for index_col in range(5):
            colonne_temp = []
            for index_row in range(5):
                colonne_temp.append(plateau[index_row][index_col])
            if colonne_temp.count("X") > 1:
                resultat["X"][str(colonne_temp.count("X"))] += 1
            if colonne_temp.count("O") > 1:
                resultat["O"][str(colonne_temp.count("X"))] += 1

        diagonale_gauche = []
        diagonale_droite = []
        for idx in range(5):
            diagonale_gauche.append(plateau[idx][idx])
            diagonale_gauche.append(plateau[idx][4 - idx])
        if diagonale_gauche.count("X") > 1:
            resultat["X"][str(diagonale_gauche.count("X"))] += 1
        if diagonale_gauche.count("O") > 1:
            resultat["O"][str(diagonale_gauche.count("X"))] += 1
        if diagonale_droite.count("X") > 1:
            resultat["X"][str(diagonale_droite.count("X"))] += 1
        if diagonale_droite.count("O") > 1:
            resultat["O"][str(diagonale_droite.count("X"))] += 1

        return resultat


    def partie_terminée(self):
        """ Retourne le nom du vainqueur une fois la partie termineé
        
        Aucun argument
        
        Return: 
            *Si la partie est terminée : nom du joueur vainqueur
            *Si la partie n'est pas terminée : None
        """
        resultat_x = self.analyser_le_plateau(self.plateau.état_plateau.get('X').get('5'))
        resultat_o = self.analyser_le_plateau(self.plateau.état_plateau.get('O').get('5'))
        if resultat_x > 0:
            return self.joueurs[0]
        if resultat_o > 0:
            return self.joueurs[1]
        return None

    def trouver_un_coup_vainqueur(self, cube):
        """Retourne un coup gagnant possible selon le symbole reçu
         
        Return: 
            *None : si aucun coup vainqueur n'est possible """

        if self.analyser_le_plateau(self.plateau.état_plateau())[cube]['4'] > 0:
            for coup in self.lister_les_coups_possibles(self.plateau.état_plateau(), cube):
                jeu_simulé = QuixoIA(self.joueurs, self.plateau.état_plateau())
                jeu_simulé.plateau.insérer_un_cube(cube, coup['origine'], coup['direction'])
                if (cube == 'X' and jeu_simulé.partie_terminée() == jeu_simulé.joueurs[0]) or (
                    cube == 'O' and jeu_simulé.partie_terminée() == jeu_simulé.joueurs[1]):
                    return coup['origine'], coup['direction']
        return None

    def trouver_un_coup_bloquant(self, cube):
        """ Troubve un coup bloquant.
        
        Return: Un coup bloquant si il y en a.
        Sinon, retourne None.
        
        """

        cube_adverse = ""
        if cube == "X":
            cube_adverse = "O"
        else:
            cube_adverse = "X"
        if self.trouver_un_coup_vainqueur(cube_adverse) is not None:
            for tentative in self.lister_les_coups_possibles(
                self.plateau.état_plateau(), cube
            ):
                jeu = QuixoIA(self.joueurs, self.plateau.état_plateau())
                jeu.plateau.insérer_un_cube(cube, tentative["origine"], tentative["direction"])
                if jeu.trouver_un_coup_vainqueur(cube_adverse) is None:
                    return (tentative["origine"], tentative["direction"])
        return None

    def jouer_un_coup(self, cube):
        """ Joue un coup.
        
        Args: cube: Le caractère utilisé par le joueur.
         
        Raise: QuixoError: la partie est déjà terminée.
               QuixoError: Le cube doit être "X" ou "O".
                
        Return: Un coup valide pour le joueur
        
        """
        if self.partie_terminée() is not None:
            raise QuixoError("La partie est déjà terminée.")
        if cube not in ["X", "O"]:
            raise QuixoError("Le cube doit être 'X' ou 'O'.")
        if self.trouver_un_coup_vainqueur(cube) is not None:
            action = self.trouver_un_coup_vainqueur(cube)
            self.déplacer_pion(cube, action[0], action[1])
            return action
        if self.trouver_un_coup_bloquant(cube) is not None:
            action = self.trouver_un_coup_bloquant(cube)
            self.déplacer_pion(cube, action[0], action[1])
            return action
        action = random.choice(self.lister_les_coups_possibles(self.plateau.état_plateau(), cube))
        self.déplacer_pion(cube, action["origine"], action["direction"])
        return(action["origine"], action["direction"])
