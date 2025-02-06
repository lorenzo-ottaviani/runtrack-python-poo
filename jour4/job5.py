from math import pi

class Forme:
    """ Classe manipulant une forme géométrique. """

    def aire(self):
        """
        Aire de la forme géométrique.
        :return: Son aire.
        """
        return 0


class Rectangle(Forme):
    """
    Classe manipulant des rectangles.
    Hérite de la classe Forme.
    """

    def __init__(self, longueur, largeur):
        """
        Initialisation de la classe.
        :param longueur: Longueur du rectangle.
        :param largeur: Largeur du rectangle.
        """
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        """
        Calcule l'aire du rectangle.
        :return: Son aire.
        """
        super().aire()
        aire = self.longueur * self.largeur
        return aire


class Cercle(Forme):
    """
    Classe manipulant des cercles.
    Hérite de la classe Forme.
    """

    def __init__(self, rayon):
        """
        Initialisation de la classe.
        :param rayon: Rayon du cercle.
        """
        self.rayon = rayon

    def aire(self):
        """
        Calcule l'aire du rectangle.
        :return: Son aire.
        """
        super().aire()
        aire = round(pi * self.rayon ** 2, 2)
        return aire


pas_carre = Rectangle(5, 6)
print(f"Je suis un rectangle. Mon aire est de {pas_carre.aire()} cm²!")

pas_de_cotes = Cercle(6)
print(f"Je suis un cercle. Mon aire est de {pas_de_cotes.aire()} cm²!")
