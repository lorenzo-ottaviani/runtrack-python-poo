class Ville:
    """ Classe qui donne des informations sur une ville. """

    def __init__(self, nom, population):
        """
        Initialisation de la classe.
        :param nom: Nom de la ville.
        :param population: Population totale de la ville.
        """
        self.__nom = nom
        self.__population = population

    def get_population(self):
        """
        Afficher la population de la ville.
        :return: La population de la ville.
        """
        return self.__population

    def set_population(self, nouvelle_population):
        """
        Modifie la population de la ville.
        :param nouvelle_population: Nouvelle population de la ville.
        :return: ∅
        """
        self.__population = nouvelle_population

class Personne:
    """ Classe qui donne des informations sur un habitant de la ville. """

    def __init__(self, nom, age, instance_ville):
        """
        Initialisation de la classe.
        :param nom: Nom de l'individu.
        :param age: Age de l'individu.
        :param instance_ville: Instance de la classe Ville.
        """
        self.__nom = nom
        self.__age = age
        self.__ville = instance_ville

    def ajouter_population(self):
        """
        Ajoute le nouvel habitant à la ville.
        :return: ∅
        """
        self.__ville.set_population(self.__ville.get_population() + 1)


# Les villes
Paris = Ville("Paris", 2113705)
Marseille = Ville("Marseille", 877215)

print(f"La population de la ville de Paris est de {Paris.get_population()} habitants.")
print(f"La population de la ville de Marseille est de {Marseille.get_population()} habitants.")

# Les habitants des villes
John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloe = Personne("Chloé", 18, Marseille)

# Mise à jour des habitants
John.ajouter_population()
Myrtille.ajouter_population()
Chloe.ajouter_population()

print(f"Après l'arrivée de John et Myrtille, il y a {Paris.get_population()} à Paris")
print(f"Après l'arrivée de Chloé, il y a {Marseille.get_population()} à Marseille")
