"""Fichier Quixo_ia

Classe:
    * QuixoIA - Classe utilisée pour jouer automatiquement contre l'ordinateur
"""
from quixo import Quixo

from plateau import Plateau

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
        if all(all(cube in {'X', 'O'} for cube in ligne) for ligne in plateau):
            raise QuixoError('La partie est déjà terminée.')
        coups_possibles = []
        for x in range(5):
            for y in range (5):
                if (x in [0, 4] or (
                    y [0, 4]) and (
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
            *Ce dictionnaire possède clés (2,3,4,5) associées au nombre de lignes de ce nombre de cube
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

    def trouver_un_coup_vainqueur(symbole):
        """Retourne un coup gagnant possible selon le symbole reçu
         
        Return: 
            *None : si aucun coup vainqueur n'est possible """


def test_analyser_le_plateau():
    # Plateau d'exemple
    entré_plateau = [
        ['O', 'X', 'X', ' ', ' '],
        ['X', 'X', 'X', 'O', ' '],
        ['O', 'X', 'O', ' ', 'O'],
        ['X', 'X', 'X', 'X', 'O'],
        ['O', ' ', 'O', ' ', ' ']
    ]
    plateau = Plateau(entré_plateau)

    # Appel de la fonction
    resultats = QuixoIA.analyser_le_plateau(plateau)

    # Résultat attendu
    attendu = {
        'X': {2: 3, 3: 4, 4: 0, 5: 0},
        'O': {2: 4, 3: 0, 4: 1, 5: 0}
    }

    # Vérification
    assert resultats == attendu, f"Erreur : {resultats} != {attendu}"

    print("Test réussi : analyser_le_plateau fonctionne correctement.")

# Exécuter le test
test_analyser_le_plateau()
