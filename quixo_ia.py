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


        for y, ligne in enumerate(plateau, start=1):
            for x, case in enumerate(ligne, start=1):
                if case == ' ' or case == cube:
                    directions = []

                    if x == 1: 
                        directions.append('droite')
                    if x == 5:
                        directions.append('gauche')
                    if y == 1:
                        directions.append('bas')
                    if y == 5:
                        directions.append('haut')

                    for direction in directions:
                        coups_possibles.append({'origine': [x, y], 'direction': direction})

        return coups_possibles


    def analyser_le_plateau(plateau):
        """ Liste pour chaque joueur, le nombre de lignes de 2,3,4 et 5 cubes qu'il possède
        Args: 
            *plateau

        Return:
            *Dictionnaire contenant les clés 'X' et 'O' associées à un dictionnaire
            *Ce dictionnaire possède clés (2,3,4,5) associées au nombre de lignes de ce nombre de cube
            """
        

    def partie_terminée(self):
        """ Retourne le nom du vainqueur une fois la partie termineé
        
        Aucun argument
        
        Return: 
            *Si la partie est terminée : nom du joueur vainqueur
            *Si la partie n'est pas terminée : None
        """
        for ligne in self.plateau:
            for i in range(len(ligne) - 4):
                if ligne[i] == ligne[i+1] == ligne[i+2] == ligne[i+3] == ligne[i+4] and ligne[i] is not None:
                    return ligne[i]

        for colonne in range(len(self.plateau[0])):
            for ligne in range(len(self.plateau) - 4):
                if self.plateau[ligne][colonne] == (
                    self.plateau[ligne+1][colonne]) == (
                        self.plateau[ligne+2][colonne]) == (
                            self.plateau[ligne+3][colonne]) == (
                                self.plateau[ligne+4][colonne]) and (
                                    self.plateau[ligne][colonne] is not None):
                    return self.plateau[ligne][colonne]

        for ligne in range(4, len(self.plateau)):
            for colonne in range(len(self.plateau[0]) - 4):
                if self.plateau[ligne][colonne] == (
                    self.plateau[ligne-1][colonne+1]) == (
                        self.plateau[ligne-2][colonne+2]) == (
                            self.plateau[ligne-3][colonne+3]) == (
                                self.plateau[ligne-4][colonne+4]) and (
                                    self.plateau[ligne][colonne] is not None):
                    return self.plateau[ligne][colonne]
                
        for ligne in range(len(self.plateau, - 4)):
            for colonne in range(len(self.plateau[0]) - 4):
                if self.plateau[ligne][colonne] == (
                    self.plateau[ligne+1][colonne+1]) == (
                        self.plateau[ligne+2][colonne+2]) == (
                            self.plateau[ligne+3][colonne+3]) == (
                                self.plateau[ligne+4][colonne+4]) and (
                                    self.plateau[ligne][colonne] is not None):
                    return self.plateau[ligne][colonne]
    
        return None

    def trouver_un_coup_vainqueur(symbole):
        """Retourne un coup gagnant possible selon le symbole reçu
         
        Return: 
            *None : si aucun coup vainqueur n'est possible """
        