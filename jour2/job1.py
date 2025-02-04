class Rectangle:
    """ Classe qui crée un rectangle. """

    def __init__(self, longueur, largeur):
        """ Initialisation de la classe. """
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        """
        Affiche la longueur du rectangle.
        :return: Sa longueur.
        """
        return self.__longueur

    def get_largeur(self):
        """
        Affiche la largeur du rectangle.
        :return: Sa largeur.
        """
        return self.__largeur

    def set_longueur(self, nouvelle_longueur):
        """
        Modifie la longueur du rectangle.
        :param nouvelle_longueur: La nouvelle longueur pour la mise à jour.
        :return: Sa nouvelle longueur.
        """
        self.__longueur = nouvelle_longueur
        return self.__longueur

    def set_largeur(self, nouvelle_largeur):
        """
        Modifie la largeur du rectangle.
        :param nouvelle_largeur: La nouvelle largeur pour la mise à jour.
        :return: Sa nouvelle largeur.
        """
        self.__largeur = nouvelle_largeur
        return self.__largeur


rectangoulous = Rectangle(10, 5)

print(f"Ma longueur est : {rectangoulous.get_longueur()}")
print(f"Ma largeur est : {rectangoulous.get_largeur()}")

print(f"Ma nouvelle longueur est : {rectangoulous.set_longueur(50)}")
print(f"Ma nouvelle largeur est : {rectangoulous.set_largeur(25)}")
