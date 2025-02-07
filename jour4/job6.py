class Vehicule:
    """ Classe permettant de manipuler des véhicules motorisés. """

    def __init__(self, marque, modele, annee, prix):
        """
        Initialisation de la classe.
        :param marque: Marque du véhicule.
        :param modele: Son modèle.
        :param annee: Année de première immatriculation.
        :param prix: Son prix.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informations_vehicule(self):
        """
        Permet d'afficher des informations détaillées sur un véhicule.
        :return: Les informations sur le véhicule.
        """
        infos = (f"Informations sur ce véhicule\nMarque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\n"
                 f"Prix : {self.annee}\n")
        return infos


class Voiture(Vehicule):
    """
    Classe qui manipule des voitures.
    Hérite de la classe Véhicule.
    """

    def __init__(self, marque, modele, annee, prix):
        """
        Initialisation de la classe.
        :param marque: Marque du véhicule.
        :param modele: Son modèle.
        :param annee: Année de première immatriculation.
        :param prix: Son prix.
        """
        super().__init__(marque, modele, annee, prix)
        self.portes = 5

    def informations_vehicule(self):
        """
        Permet d'afficher des informations détaillées sur une voiture.
        :return: Les informations sur la voiture.
        """
        super().informations_vehicule()
        infos = (f"Informations sur cette voiture\nMarque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\n"
                 f"Prix : {self.annee}\nNombre de portes : {self.portes}")
        return infos


class Moto(Vehicule):
    """
    Classe qui manipule des motos.
    Hérite de la classe Véhicule.
    """

    def __init__(self, marque, modele, annee, prix):
        """
        Initialisation de la classe.
        :param marque: Marque du véhicule.
        :param modele: Son modèle.
        :param annee: Année de première immatriculation.
        :param prix: Son prix.
        """
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informations_vehicule(self):
        """
        Permet d'afficher des informations détaillées sur une moto.
        :return: Les informations sur la moto.
        """
        super().informations_vehicule()
        infos = (f"Informations sur cette voiture\nMarque : {self.marque}\nModele : {self.modele}\nAnnee : {self.annee}\n"
                 f"Prix : {self.annee}\nNombre de roues : {self.roue}")
        return infos


raptor = Voiture("Cornus", "Titan", 1983, 153000)
print(raptor.informations_vehicule(), end="\n\n")

titus = Moto("Copper", "Rubra", 2018, 7896)
print(titus.informations_vehicule())
