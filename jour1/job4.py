class Personne:
    """ Classe qui donne des informations sur des individus."""
    def __init__(self, prenom="Gérard", nom="Torche"):
        """ Initialisation de la classe."""
        self.prenom = prenom
        self.nom = nom

    def se_presenter(self):
        """
        Méthode pour présenter une personne.
        :return: Présentation de la personne.
        """
        return f"Je suis {self.prenom} {self.nom}"


individu_1 = Personne()
print(individu_1.se_presenter())

individu_2 = Personne("Coralie", "Raptor")
print(individu_2.se_presenter())

individu_3 = Personne("Crotte", "Puante")
print(f"{individu_3.se_presenter()}, je suis désolée c'est moi qui a intoxiqué la Broadcast Room!")
