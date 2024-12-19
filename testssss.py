from plateau import Plateau


def analyser_le_plateau(plateau):
        """ Liste pour chaque joueur, le nombre de lignes de 2,3,4 et 5 cubes qu'il possède
        Args: 
            *plateau

        Return:
            *Dictionnaire contenant les clés 'X' et 'O' associées à un dictionnaire
            *Ce dictionnaire possède clés (2,3,4,5) associées au nombre de lignes de ce nombre de cube
            """
        resultats = {'X': {2: 0, 3: 0, 4: 0, 5: 0},
                 'O': {2: 0, 3: 0, 4: 0, 5: 0}}
        grille = plateau.état_plateau()
        for ligne in grille:
            for joueur in ['X', 'O']:
                for taille in range(2, 6):
                    if ligne.count(joueur) == taille and ligne.count(' ') == len(ligne) - taille:
                        resultats[joueur][taille] += 1

        for x in range(5):
            colonne = [grille[y][x] for y in range(5)]
            for joueur in ['X', 'O']:
                for taille in range(2, 6):
                    if colonne.count(joueur) == taille and colonne.count(' ') == len(colonne) - taille:
                        resultats[joueur][taille] += 1
        diagonales = [
            [grille[i][i] for i in range(5)],
            [grille[i][4 - i] for i in range(5)]
        ]
        for diag in diagonales:
            for joueur in ['X', 'O']:
                for taille in range(2, 6):
                    if diag.count(joueur) == taille and diag.count(' ') == len(diag) - taille:
                        resultats[joueur][taille] += 1
        
        return resultats

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
    resultats = analyser_le_plateau(plateau)

    # Résultat attendu
    attendu = {
        'X': {2: 4, 3: 3, 4: 2, 5: 0},
        'O': {2: 6, 3: 2, 4: 0, 5: 0}
    }

    # Vérification
    assert resultats == attendu, f"Erreur : {resultats} != {attendu}"

    print("Test réussi : analyser_le_plateau fonctionne correctement.")

# Exécuter le test
test_analyser_le_plateau()