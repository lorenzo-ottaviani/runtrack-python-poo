from math import pi
import turtle


class Cercle:
    """ Classe qui crée des cercles."""

    def __init__(self, rayon=1):
        """ Initialisation de la classe."""
        self.rayon = rayon

    def changer_rayon(self, nouveau_rayon):
        """
        Permet de changer le rayon du cercle.
        :return: Le nouveau rayon.
        """
        self.rayon = nouveau_rayon
        return self.rayon

    def circonference(self):
        """
        Permet de calculer la circonférence du cercle.
        :return: La circonférence du cercle arrondi à 10^-2.
        """
        return round(self.rayon * 2 * pi, 2)

    def aire(self):
        """
        Permet de calculer l'aire du cercle.
        :return: L'aire' du cercle arrondi à 10^-2.
        """
        return round(pi * self.rayon ** 2, 2)

    def diametre(self):
        """
        Permet de calculer le diamètre du cercle.
        :return: Le diamètre du cercle.
        """
        return 2 * self.rayon

    def afficher_infos(self):
        """
        Afficher toutes les informations du cercle.
        :return: Les infos du cercle.
        """
        infos = (f"Mon rayon est : {self.rayon}\nMon diamètre est : {self.diametre()}"
                 f"\nMa circonférence est : {self.circonference()}\nMon aire est : {self.aire()}\n")
        return infos


# Infos du cercle
circulus = Cercle(5)
print(circulus.afficher_infos())

# Dessin du cercle
turtle.dot(10, 'black')
turtle.up()
turtle.goto(0, - circulus.rayon * 50)
turtle.down()
turtle.color('blue')
turtle.width(3)
turtle.circle(circulus.rayon * 50)
turtle.hideturtle()
turtle.done()
