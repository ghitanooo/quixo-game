"""Jeu Quixo

Ce programme permet de joueur au jeu Quixo.
"""

from api import initialiser_partie, jouer_un_coup, récupérer_une_partie
from quixo import Quixo, interpréter_la_commande
from quixo_ia import QuixoIA

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = "022e3869-9ddf-4aab-bf5c-b3b6f017ec07"


if __name__ == "__main__":
    args = interpréter_la_commande()
    id_partie, joueurs, plateau = initialiser_partie(args.idul, SECRET)
    while True:
        try:
            if args.autonome is False:
                # Créer une instance de Quixo
                quixo = Quixo(joueurs, plateau)
                # Afficher la partie
                print(quixo)
                # Demander au joueur de choisir son prochain coup
                origine, direction = quixo.choisir_un_coup()
                # Envoyez le coup au serveur
                id_partie, joueurs, plateau = jouer_un_coup(
                    id_partie,
                    origine,
                    direction,
                    args.idul,
                    SECRET,
                )
            else:
                quixo = QuixoIA(joueurs, plateau)
                print(quixo)
                origine, direction = quixo.jouer_un_coup('X')
                print(quixo)
                id_partie, joueurs, plateau = jouer_un_coup(
                    id_partie,
                    origine,
                    direction,
                    args.idul,
                    SECRET,
                )
        except StopIteration:
            id_partie, joueurs, plateau, vainqueur = récupérer_une_partie(
                id_partie,
                args.idul,
                SECRET,
            )
            if vainqueur == 'IA':
                quixo = Quixo(joueurs, plateau)
                print(quixo)
            print('Le gagnant est: ' + vainqueur)
            break
