class Livre:
    """ Classe qui crée un livre. """

    def __init__(self, titre, auteur, nombre_pages, disponible=True):
        """ Initialisation de la classe. """
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_pages = nombre_pages
        self.__disponible = disponible

    def get_titre(self):
        """
        Affiche le titre du livre.
        :return: Son titre.
        """
        return self.__titre

    def get_auteur(self):
        """
        Affiche l'auteur du livre.
        :return: Son auteur.
        """
        return self.__auteur

    def get_nombre_pages(self):
        """
        Affiche le nombre de pages du livre.
        :return: Son nombre de pages.
        """
        return self.__nombre_pages

    def set_titre(self, nouveau_titre):
        """
        Modifie le titre du livre.
        :param nouveau_titre: Le nouveau titre du livre.
        :return: ∅
        """
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        """
        Modifie l'auteur du livre.
        :param nouvel_auteur: Le nouvel auteur du livre.
        :return: ∅
        """
        self.__auteur = nouvel_auteur

    def set_nombre_pages(self, nouveau_nombre_pages):
        """
        Modifie le nombre de pages du livre.
        :param nouveau_nombre_pages: Le nouveau nombre de pages du livre
        :return: ∅
        """
        try:
            nouveau_nombre_pages = int(nouveau_nombre_pages)
            if nouveau_nombre_pages > 0:
                self.__nombre_pages = nouveau_nombre_pages
            else:
                print("L'Entrée n'est pas correcte : ce n'est pas un entier positif!")
        except ValueError:
            print("L'Entrée n'est pas correcte : ce n'est pas un nombre entier!")

    def verification(self):
        """
        Vérifie si le livre est disponible.
        :return: La disponibilité du livre.
        """
        if self.__disponible:
            verifier = True
        else:
            verifier = False

        return verifier

    def emprunter(self):
        """
        Permet d'emprunter un livre s'il est disponible.
        :return: ∅
        """
        if self.verification():
            print("Emprunt éffectué avec succès! Bonne lecture!")
            self.__disponible = False
        else:
            print("Ce volume n'est pas disponible en ce moment.")


    def rendre(self):
        """
        Permet de restituer un livre s'il est disponible.
        :return: ∅
        """
        if not self.verification():
            print(f"Livre réstitué! {self.get_titre()} est de nouveau disponible à l'emprunt.")
            self.__disponible = True
        else:
            print("Ce volume n'avait pas été emprunté.")



tardigrade = Livre("L'incroyable vie du tardigrade", "Tardigrade Suprème", 453)

tardigrade.set_nombre_pages(-100)
tardigrade.set_nombre_pages("xxx")
tardigrade.set_nombre_pages(888)

print(f"{tardigrade.get_nombre_pages()}\n")

tardigrade.emprunter()
tardigrade.emprunter()
print()

tardigrade.rendre()
tardigrade.rendre()
