class Carte:
    """ Classe qui manipule des cartes de jeu. """

    def __init__(self, valeur, couleur):
        """
        Initialisation de la classe.
        :param valeur: Valeur de la carte (numéro).
        :param couleur: Sa couleur.
        """
        self.valeur = valeur
        self.couleur = couleur


class Jeu(Carte):
    """ Classe qui gère le jeu du Blackjack. """

    def __init__(self, valeur, couleur):
        """"""
        super().__init__(valeur, couleur)
        self.paquet = []
