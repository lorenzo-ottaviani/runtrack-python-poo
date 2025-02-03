def point_input():
    """
    Fonction pour entrer une coordonnée d'un point
    :return: La coordonnée
    """
    test = False
    while not test:
        try:
            valeur = float(input("Entrer votre coordonnée : "))
            test = True
        except ValueError:
            print("Les coordonnées x et y doivent être des nombres!")
    return valeur


class Point:
    """ Classe pour faire des points. """
    def __init__(self, x, y):
        """ Initialisation de la classe."""
        self.x = x
        self.y = y

    def affiche_point(self):
        """
        Affiche les coordonnées du point.
        :return: Les coordonnées du point.
        """
        return f"({self.x} , {self.y})"

    def affiche_x(self):
        """
        Affiche l'abscisse du point.
        :return: L'abscisse du point.
        """
        return f"Mon abscisse est {self.x}"

    def affiche_y(self):
        """
        Affiche l'ordonnée du point.
        :return: L'ordonnée du point.
        """
        return f"Mon ordonnée est {self.y}"

    def changer_x(self, x_bis):
        """
        Permet de changer l'abscisse du point.
        :param x_bis: Nouvelle valeur de l'abscisse.
        :return: ∅
        """
        self.x = x_bis

    def changer_y(self, y_bis):
        """
        Permet de changer l'ordonnée du point.
        :param y_bis: Nouvelle valeur de l'ordonnée.
        :return: ∅
        """
        self.y = y_bis


print("Bonjour!\nOn va créer le point A")
A = Point(point_input(), point_input())
print(f"Je suis le point A j'habite en {A.affiche_point()}")
print(A.affiche_x())
print(A.affiche_y())
A.changer_x(point_input())
A.changer_y(point_input())
print(A.affiche_x())
print(A.affiche_y())

print("Et maintenant: on va créer le point B")
B = Point(point_input(), point_input())
print(f"Je suis le point B j'habite en {B.affiche_point()}")
print(B.affiche_x())
print(B.affiche_y())
B.changer_x(point_input())
B.changer_y(point_input())
print(B.affiche_x())
print(B.affiche_y())
