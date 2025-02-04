class Voiture:
    """ Classe qui manipule des données sur une voiture. """

    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        """ Initialisation de la classe. """
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche

    def get_marque(self):
        """
        Affiche la marque de la voiture.
        :return: Sa marque.
        """
        return self.__marque

    def set_marque(self, nouvelle_marque):
        """
        Modifie la marque de la voiture.
        :param nouvelle_marque: La nouvelle marque de la voiture.
        :return: ∅
        """
        self.__marque = nouvelle_marque

    def get_modele(self):
        """
        Affiche le modèle de la voiture.
        :return: Son modèle.
        """
        return self.__modele

    def set_modele(self, nouveau_modele):
        """
        Modifie le modèle de la voiture.
        :param nouveau_modele: Le nouveau modèle de la voiture.
        :return: ∅
        """
        self.__modele = nouveau_modele

    def get_annee(self):
        """
        Affiche l'année de la voiture.
        :return: Son année.
        """
        return self.__annee

    def set_annee(self, nouvelle_annee):
        """
        Modifie l'année de la voiture.
        :param nouvelle_annee: La nouvelle année de la voiture.
        :return: ∅
        """
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        """
        Affiche le kilométrage de la voiture.
        :return: Son kilométrage.
        """
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        """
        Modifie le kilométrage de la voiture.
        :param nouveau_kilometrage: Le nouveau kilométrage de la voiture.
        :return: ∅
        """
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        """
        Affiche si la voiture roule ou pas.
        :return: Son état actuel.
        """
        return self.__en_marche

    def demarrer(self):
        """
        Permet de démarrer la voiture.
        :return: ∅
        """
        if not self.__en_marche:
            self.__en_marche = True
            print("Voiture démarrée !")
        else:
            print("La voiture roule déjà, le chien est parti sans toi!")

    def arreter(self):
        """
        Permet d'arrêter la voiture.
        :return: ∅
        """
        if self.__en_marche:
            self.__en_marche = False
            print("Voiture arrêtée !")
        else:
            print("La voiture est déjà arrêté! Tu fais quoi !? Il est temps d'aller dormir!")


caisse = Voiture("Raptor", "Citrus", 1730, 150354)
print(caisse.get_marque())
caisse.set_marque("Marquise")
print(caisse.get_marque())

print(f"L'état de marche de la voiture est : {caisse.get_en_marche()}\n")
caisse.demarrer()
caisse.demarrer()

print()
caisse.arreter()
caisse.arreter()
