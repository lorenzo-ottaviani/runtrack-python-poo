class Rectangle:
    """ Classe qui gère des données sur des rectangles. """

    def __init__(self, longueur, largeur):
        """
        Initialisation de la classe.
        :param longueur: Longueur du rectangle.
        :param largeur: Largeur du rectangle.
        """
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        """
        Affiche la longueur du rectangle.
        :return: Sa longueur.
        """
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        """
        Affiche la longueur du rectangle.
        :param nouvelle_longueur: La nouvelle longueur du rectangle.
        :return: ∅
        """
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        """
        Affiche la largeur du rectangle.
        :return: Sa largeur.
        """
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        """
        Affiche la longueur du rectangle.
        :param nouvelle_largeur: La nouvelle largeur du rectangle.
        :return: ∅
        """
        self.__largeur = nouvelle_largeur

    def perimetre(self):
        """
        Calcule le périmètre du rectangle.
        :return: Son périmètre.
        """
        perimetre = (self.__longueur + self.__largeur) * 2
        return perimetre

    def aire(self):
        """
        Calcule l'aire du rectangle.
        :return: Son aire.
        """
        aire = self.__longueur * self.__largeur
        return aire


class Parallepipede(Rectangle):
    """
    Classe qui gère des données sur des parallélépipèdes.
    Hérite de la classe Rectangle.
    """

    def __init__(self, longueur, largeur, hauteur):
        """
        Initialisation de la classe.
        :param longueur: La longueur du parallélépipède.
        :param largeur: Sa largeur.
        :param hauteur: Son hauteur.
        """
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        """
        Calcule le volume du parallélépipède.
        :return: Son volume.
        """
        volume = self.get_longueur() * self.get_largeur() * self.hauteur
        return volume


# Information de base de rectangoulous
rectangoulous = Rectangle(10, 5)
print(f"Sa longueur : {rectangoulous.get_longueur()} cm")
print(f"Sa largeur : {rectangoulous.get_largeur()} cm")

# Modifications et calculs de rectangoulous
rectangoulous.set_longueur(40)
rectangoulous.set_largeur(28)
print(f"Son aire : {rectangoulous.aire()} cm²")
print(f"Son périmètre : {rectangoulous.perimetre()} cm")

# C'est un gros pavé
pave = Parallepipede(6, 3, 4)
print(f"\nOh! Quel pavé! Il est vraiment gros celui là!\nSon volume est de {pave.volume()} cm3")
