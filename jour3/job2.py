class CompteBancaire:
    """ Classe qui permet de gérer un compte bancaire. """

    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        """
        Initialisation de la classe.
        :param numero_compte: Numéro du compte de la personne.
        :param nom: Son nom.
        :param prenom: Son prénom.
        :param solde: Le solde de son compte.
        """
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        """
        Affiche les informations du compte du client.
        :return: Les infos du compte.
        """
        infos = (f"Informations du compte n° {self.__numero_compte} :\nNom : {self.__nom}\nPrénom : {self.__prenom}\n"
                 f"Solde actuel : {self.__solde}\n")
        return infos

    def afficher_solde(self):
        """
        Affiche le solde du compte.
        :return: Le solde du compte.
        """
        return self.__solde

    def get_numero_compte(self):
        """
        Affiche le numéro du compte.
        :return: Le numéro du compte.
        """
        return self.__numero_compte

    def versement(self, montant):
        """
        Ajoute un versement au compte du client.
        :param montant: Montant versé.
        :return: ∅
        """
        self.__solde += montant

    def retrait(self, montant):
        """
        Retire si possible un montant du compte du client.
        :param montant: Montant à retirer.
        :return: ∅
        """
        if self.__decouvert:
            self.__solde = self.__solde - montant

        else:
            if (self.__solde - montant) < 0:
                print("Retrait supérieur au solde! Madoff ne prête pas, il vole juste votre argent!")

            else:
                self.__solde = self.__solde - montant

    def changer_statut_decouvert(self):
        """
        Change le statut du découvert (interdit si autorisé, sinon l'inverse).
        :return: ∅
        """
        self.__decouvert = True if self.__decouvert is False else False

    def agios(self):
        """
        Calcule les agios liés au découvert du compte.
        :return: Le montant des agios.
        """
        if self.__solde < 0:
            agios = abs(self.__solde) * 1.5
            print("Madoff vous impose son tarif! t'avais qu'à pas être en découvert! 150 % d'agios!!\n")
            return agios
        else:
            print("Dommage, vous n'êtes pas à découvert, ce sera pour la prochaine fois!")

    def virement(self, reference, compte_beneficiaire, montant):
        """
        Effectue un virement d'un compte à un autre.
        :return:
        """
        if (self.__solde - montant) > 0:
            self.retrait(montant)
            compte_beneficiaire.versement(montant)
            print("Virement effectué avec succès.")

        else:
            print("Virement impossible, tu n'as pas assez de fric pour ça!")


# Compte de Georgette
georgette = CompteBancaire("000024783", "Tahrkut", "Georgette", 30743)

print("Bienvenue chez Madoff's Banking!\n")
print(georgette.afficher())

georgette.versement(10718)
print(georgette.afficher())

# Compte de Baptiste
baptiste = CompteBancaire("000043101", "Kartum", "Baptiste", 141)
baptiste.retrait(200)
baptiste.changer_statut_decouvert()
baptiste.retrait(200)
print(f"\nVos agios pour un découvert de {baptiste.afficher_solde()} euros sont : {baptiste.agios()} euros.")
