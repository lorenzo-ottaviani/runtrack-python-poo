class Personnage:
    """ Classe qui gère des personnages d'un jeu. """

    def __init__(self, nom):
        """
        Initialisation de la classe.
        :param nom: Nom du personnage.
        """
        self.nom = nom
        self.vie = 0

    def attaquer(self, adversaire):
        """
        Attaque l'adversaire et lui enlève un point de vie.
        :param adversaire: L'adversaire.
        :return: ∅
        """
        adversaire.vie -= 1


class Jeu:
    """ Classe qui gère le jeu de combat."""

    def __init__(self):
        """"""
        self.niveau = 0
        self.joueur = Personnage("Petit chaton")
        self.adversaire = Personnage("Tyrannosaurus rex")

    def choisir_niveau(self, niveau):
        """
        Permet de choisir le niveau de difficulté du jeu.
        :param niveau: Le niveau choisi par le joueur.
        :return: ∅
        """
        self.niveau = niveau

    def lancer_jeu(self):
        """
        Permet de préparer les paramètres du jeu afin d'y jouer.
        :return: ∅
        """
        if self.niveau == 1:
            self.joueur.vie = 10
            self.adversaire.vie = 3

        elif self.niveau == 2:
            self.joueur.vie = 5
            self.adversaire.vie = 5

        elif self.niveau == 3:
            self.joueur.vie = 2
            self.adversaire.vie = 10

    def verifier_sante(self):
        """
        Affiche la santé de chacun des joueurs.
        :return: Leur état de santé
        """
        infos = (f"Le {self.joueur.nom} a {self.joueur.vie} PV tandis que le {self.adversaire.nom} a "
                 f"{self.adversaire.vie} PV")
        return infos

    def victoire(self):
        """
        Teste si les conditions de victoire sont atteintes et détermine quel joueur a gagné.
        :return: True s'il y a une victoire sinon False.
        """
        if self.adversaire.vie == 0:
            print(f"Le {self.joueur.nom} a gagné!")
            victoire = True
        elif self.joueur.vie == 0:
            print(f"Le {self.adversaire.nom} a gagné!")
            victoire = True
        else:
            victoire = False
        return victoire

    def jouer_un_tour(self):
        """
        Permet de jouer un tour du jeu.
        :return: ∅
        """
        self.joueur.attaquer(self.adversaire)
        print(self.verifier_sante())

        if not self.victoire():  # Vérifie s'il y a une victoire après l'attaque du joueur
            self.adversaire.attaquer(self.joueur)
            print(self.verifier_sante())
            self.victoire()  # Vérifie s'il y a une victoire après l'attaque de l'adversaire


def main():
    """
    Fonction principale du jeu.
    :return: ∅
    """
    tour = 1
    jeu = Jeu()
    jeu.choisir_niveau(2)
    jeu.lancer_jeu()

    while not jeu.victoire():
        print(f"\nTour n°{tour}")
        jeu.jouer_un_tour()
        tour += 1


if __name__ == "__main__":  # Évite que le programme puisse être lancé depuis un autre programme.
    main()
