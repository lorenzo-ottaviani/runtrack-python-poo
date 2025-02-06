class Personne:
    """ Classe qui gère des informations sur des individus. """

    def __init__(self):
        """ Initialisation de la classe. """
        self.__age = 14

    def afficher_age(self):
        """
        Affiche l'âge de la personne.
        :return: L'âge de la personne.
        """
        return self.__age

    def modifier_age(self, nouvel_age):
        """
        Modifie l'âge de la personne.
        :param nouvel_age: Le nouvel âge à lui attribuer.
        :return: ∅
        """
        self.__age = nouvel_age

    def bonjour(self):
        """
        Présente une personne.
        :return: Affiche "Hello".
        """
        return "Hello."


class Eleve(Personne):
    """
    Classe qui gère des élèves.
    Hérite de la classe Personne.
    """

    def __init__(self):
        """ Initialisation de la classe. """
        super().__init__()

    def aller_en_cours(self):
        """
        Informe si un élève va en cours.
        :return: Affiche "Je vais en cours".
        """
        return "Je vais en cours."

    def afficher_age(self):
        """"""
        return f"J'ai {super().afficher_age()} ans."


class Professeur:
    """ Classe qui gère des enseignants."""

    def __init__(self, matiere_enseignee):
        """ Initialisation de la classe. """
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        """
        Annonce le début du cours.
        :return: Affiche "Le cours va commencer".
        """
        return "Le cours va commencer."


patrick = Personne()
print(patrick.bonjour())

cyril = Eleve()
print(cyril.afficher_age())
