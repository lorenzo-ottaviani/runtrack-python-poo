class Commande:
    """ Classe qui permet de gérer une commande. """

    def __init__(self, numero_commande, liste_plats, statut_commande):
        """ Initialisation de la classe. """
        self.__numero_commande = numero_commande
        self.__liste_plats = liste_plats
        self.__statut_commande = statut_commande
        self.__dico_prix = {"statut commande": self.__statut_commande, "pieds et paquets": 18.50, "tofu sauté": 17.80,
                            "pression": 3.00, "monaco allégé": 6.25, "cake sans gluten": 27.35, "café": 2.5,
                            "rat en timbale": 38.75}

    def ajouter_plat(self, plat):
        """
        Permet d'ajouter un plat à la commande.
        :param plat: Plat à ajouter à la liste des plats.
        :return: ∅
        """
        return self.__liste_plats.append(plat)

    def annulation(self):
        """
        Permet d'annuler la commande en cours.
        :return:
        """
        if self.__statut_commande != "Annulée":
            self.__statut_commande = "Annulée"
            self.__dico_prix["statut commande"] = "Annulée"
            print("Commande annulée")
        else:
            print("Commande déjà annulée par la direction, client expulsé, chiens enragés lâchés!")

    def __prix_total(self):
        """
        Permet de calculer le prix total de la commande.
        :return: Prix total de la commande.
        """
        total = 0
        if self.__dico_prix["statut commande"] == "Annulée":
            print("Commande annulée! Rien à payer! Client à expulser!!")
        else:
            for plat_menu in self.__dico_prix:
                for plat_client in self.__liste_plats:
                    if plat_menu == plat_client:
                        total += self.__dico_prix[plat_menu]
            self.__statut_commande = "Terminée"
            return total

    def get_prix_total(self):
        """
        Affiche le prix total de la commande.
        :return: Le prix total.
        """
        return self.__prix_total()

    def TVA(self):
        """
        Calcule la TVA de la commande.
        :return: La TVA.
        """
        prix_HT = self.__prix_total() / 1.20
        TVA = self.__prix_total() - prix_HT
        return round(TVA, 2)


sandrine = Commande(37, ["pieds et paquets", "tofu sauté", "monaco allégé", "cake sans gluten"],
                    "en cours")
print(f"\nVotre addition est de : {sandrine.get_prix_total()} euros.")
print(f"La TVA est de : {sandrine.TVA()} euros.\n")

sandrine.annulation()
sandrine.annulation()
print(f"\nVotre addition est de : {sandrine.get_prix_total()} euros.")
