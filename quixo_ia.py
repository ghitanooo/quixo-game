"""Fichier Quixo_ia

Classe:
    * QuixoIA - Classe utilisée pour jouer automatiquement contre l'ordinateur
"""


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

        if all(all(cube in {'X', 'O'} for cube in ligne) for ligne in Plateau.plateau):
            raise QuixoError('La partie est déjà terminée.')

        coups_possibles = []


        taille = len(plateau.plateau)

        for y, ligne in enumerate(plateau.Plateau, start=1):
            for x, case in enumerate(ligne, start=1):
                if case == ' ' or case == cube:
                    directions = []

                    if (x, y) in [(1, 1), (1, taille), (taille, 1), (taille, taille)]:
                        if x == 1: 
                            directions.append('droite')
                        else:
                            directions.append('gauche')
                        if y == 1:
                            directions.append('bas')
                        else:
                            directions.append('haut')

                    elif x == 1 or x == taille or y == 1 or y == taille:
                        if x == 1:
                            directions.extend(['droite', 'haut', 'bas'])
                        elif x == taille:
                            directions.extend(['gauche', 'haut', 'bas'])
                        if y == 1:
                            directions.extend(['droite', 'gauche', 'bas'])
                        elif y == 1:
                            directions.extend(['droite', 'gauche', 'haut'])

                    for direction in directions:
                        coups_possibles.append({'origine': [x, y], 'direction': direction})

        return coups_possibles

        

    def analyser_le_plateau(plateau):
        """ 
        """


