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
    def lister_les_coups_possibles(plateau, symbole):
        """Lister tous les coups possibles dans une partie

        Args: 
            * Un plateau de jeu
            * Symbole du cube représentant le joueur

        Return:
            *Liste de dictionnaires des coups possibles pour le joueur spécifié

        Raise: 
            *QuixoError si le cube n'est pas valide, ou si la parties est terminée
        """
        

