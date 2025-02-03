class Produit:
    """ Classe qui crée des cercles."""

    def __init__(self, nom, prix_HT, TVA):
        """ Initialisation de la classe."""
        self.nom = nom
        self.prix_HT = prix_HT
        self.TVA = TVA

    def calculer_prix_TTC(self):
        """
        Permet de calculer le prix TTC (Toutes Taxes Comprises) d'un produit.
        :return: Le prix TTC.
        """
        prix_TTC = self.prix_HT * (1 + self.TVA / 100)
        return round(prix_TTC, 2)

    def afficher(self):
        """
        Afficher toutes les informations du produit.
        :return: Les infos du produit.
        """
        infos = (f"Le produit est : {self.nom}\nMon prix HT est : {self.prix_HT}"
                 f"\nMa TVA est : {self.TVA} %\nMon prix TTC est : {self.calculer_prix_TTC()}\n")
        return infos

    def modifier_prix(self, nouveau_prix):
        """
        Modifie le prix d'un produit.
        :param nouveau_prix: Le nouveau prix du produit.
        :return: Le nouveau prix.
        """
        self.prix_HT = nouveau_prix
        return self.prix_HT

    def modifier_nom(self, nouveau_nom):
        """
        Modifie le nom d'un produit.
        :param nouveau_nom: Le nouveau nom du produit.
        :return: Le nouveau nom.
        """
        self.nom = nouveau_nom
        return self.nom


# Premier produit
produit_1 = Produit("fer", 28.53, 40)
print(produit_1.afficher())
produit_1.modifier_nom("cuivre")
produit_1.modifier_prix(10.05)
print(produit_1.afficher())

# Second produit
produit_2 = Produit("choucroute périmée", 28.30, 5)
print(produit_2.afficher())
produit_2.modifier_nom("concombre moisi")
produit_2.modifier_prix(7.83)
print(produit_2.afficher())

# Troisième produit
produit_3 = Produit("crabe", 5.55, 20)
print(produit_3.afficher())
produit_3.modifier_nom("langouste")
produit_3.modifier_prix(47.19)
print(produit_3.afficher())
