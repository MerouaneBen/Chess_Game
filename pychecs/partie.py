# -*- coding: utf-8 -*-
"""Ce module contient une classe contenant les informations sur une partie d'échecs,
dont un objet échiquier (une instance de la classe Echiquier).

"""
from pychecs.echiquier import Echiquier


class Partie:
    """La classe Partie contient les informations sur une partie d'échecs, c'est à dire un échiquier, puis
    un joueur actif (blanc ou noir). Des méthodes sont disponibles pour faire avancer la partie et interagir
    avec l'utilisateur.

    Attributes:
        joueur_actif (str): La couleur du joueur actif, 'blanc' ou 'noir'.
        echiquier (Echiquier): L'échiquier sur lequel se déroule la partie.

    """
    def __init__(self):
        # Le joueur débutant une partie d'échecs est le joueur blanc.
        self.joueur_actif = 'blanc'

        # Création d'une instance de la classe Echiquier, qui sera manipulée dans les méthodes de la classe.
        self.echiquier = Echiquier()

    def determiner_gagnant(self):
        """Détermine la couleur du joueur gagnant, s'il y en a un. Pour déterminer si un joueur est le gagnant,
        le roi de la couleur adverse doit être absente de l'échiquier.

        Returns:
            str: 'blanc' si le joueur blanc a gagné, 'noir' si c'est plutôt le joueur noir, et 'aucun' si aucun
                joueur n'a encore gagné.

        """

        if not self.echiquier.roi_de_couleur_est_dans_echiquier(partie.joueur_actif) and self.echiquier.roi_de_couleur_est_dans_echiquier('noir'):
            return 'noir'
        elif self.echiquier.roi_de_couleur_est_dans_echiquier(partie.joueur_actif) and not self.echiquier.roi_de_couleur_est_dans_echiquier('noir') :
            return 'blanc'
        else:
            return 'aucun'

    def partie_terminee(self):
        """Vérifie si la partie est terminée. Une partie est terminée si un gagnant peut être déclaré.

        Returns:
            bool: True si la partie est terminée, et False autrement.

        """
        if partie.determiner_gagnant() != 'aucun':
            return True
        else:
            return False

    def demander_positions(self):
        """Demande à l'utilisateur d'entrer les positions de départ et d'arrivée pour faire un déplacement. Si les
        positions entrées sont valides (si le déplacement est valide), on retourne les deux positions. On doit
        redemander tant que l'utilisateur ne donne pas des positions valides.

        Returns:
            str, str: Deux chaînes de caractères représentant les deux positions valides fournies par l'utilisateurs.

        """


        position_source = input('Veuillez rentrez une position source :')
        position_cible = input('Veuillez rentrez une position cible :')

        while not self.echiquier.deplacement_est_valide(position_source,position_cible):

            print ('\033[91m' + '\033[1m' + 'Erreurs, positions invalides!' + '\033[0m''\n')
            position_source = input('Veuillez rentrez une nouvelle position source :')
            position_cible = input ('Veuillez rentrez une nouvelle position cible :')

        return position_source, position_cible


    def joueur_suivant(self):
        """
        Change le joueur actif: passe de blanc à noir, ou de noir à blanc, selon la couleur du joueur actif.

        """


        if self.joueur_actif == 'blanc':
            joueur = self.joueur_actif = 'noir'
        else:
           joueur =  self.joueur_actif = 'blanc'

        return joueur

    def jouer(self):

        """Tant que la partie n'est pas terminée, joue la partie. À chaque tour :
            - On affiche l'échiquier.
            - On demande les deux positions.
            - On fait le déplacement sur l'échiquier.
            - On passe au joueur suivant.

        Une fois la partie terminée, on félicite le joueur gagnant!

        """
        while not partie.partie_terminee():
            print(self.echiquier) # on imprime le chiquier
            print('Tour du joueur ' + '\033[1m' + partie.joueur_actif  + '\033[0m''\n') # On identifie le joueur actif
            liste_positions = list(partie.demander_positions()) # on liste les deux positions introduites par le joueur
            if partie.joueur_actif == self.echiquier.couleur_piece_a_position(liste_positions[0]): # on vérifier si le joueur actif déplace les bonnes pieces
                self.echiquier.deplacer(liste_positions[0],liste_positions[1]) # on fait le déplacement dans l'échiquier
                partie.joueur_suivant() # on change le joueur
                partie.echiquier.dictionnaire_pieces = self.echiquier.dictionnaire_pieces # on affecte les nouvelles valeurs du dictionnaire au déctionnaires global de classe pour qu'il puisse etre utilisé par d'autre méthodes
            else:
                print('\n''\033[91m' + '\033[1m' + "Ce n'es pas votre tour!" + '\033[0m''\n')
        print('partie terminée! Félicitation au joueur ' + partie.determiner_gagnant())

partie = Partie()
    #echiquier = Echiquier()
    #print (partie.jouer())
