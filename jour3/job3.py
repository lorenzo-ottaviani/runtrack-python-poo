class Tache:
    """ Classe donnant des informations sur une tâche. """

    def __init__(self, titre, description, statut="En cours"):
        """
        Initialisation de la classe.
        :param titre: Titre de la tâche.
        :param description: Description de la tâche.
        :param statut: Statut de la tâche (à faire ou terminée).
        """
        self.titre = titre
        self.description = description
        self.statut = statut

    def afficher_tache(self):
        """"""
        infos = f"Titre de la tâche : {self.titre}\nDescription : {self.description}\nStatut : {self.statut}\n"
        return infos


class ListeDeTaches:
    """ Classe gérant une liste de tâches. """

    def __init__(self):
        """ Initialisation de la classe. """
        self.liste_taches = []

    def ajouter_tache(self, tache):
        """
        Ajoute une tâche à la liste de tâches.
        :param tache: Un objet de la classe Tâche à ajouter.
        :return: ∅
        """
        self.liste_taches.append(tache)

    def supprimer_tache(self, tache):
        """
        Supprime une tâche de la liste de tâches.
        :param tache: Objet de la classe Tâche à supprimer.
        :return: ∅
        """
        for element in self.liste_taches:
            if element == tache:
                self.liste_taches.remove(element)

    def marquer_comme_finie(self, tache):
        """"""
        for element in self.liste_taches:
            if element == tache:
                tache.statut = "Finie"
                print("Tache finie!")

    def affiche_liste(self):
        """
        Affiche la liste de tâches.
        :return: La liste de tâches
        """
        liste_affichable = [element.titre for element in self.liste_taches]
        return liste_affichable

    def filtrer_liste(self):
        """
        Filtre dans la liste uniquement la liste des tâches finies.
        :return: La liste des tâches finies.
        """
        liste_taches_finies = []
        for element in self.liste_taches:
            if element.statut == "Finie":
                liste_taches_finies.append(element.titre)
        return liste_taches_finies


souffler = Tache("Souffler", "Souffler la maison de paille du petit cochon.")
rouler = Tache("Déplacement", "Test de déplacement d'un point A à un point B.")

wolf_list = ListeDeTaches()  # Liste du grand méchant loup

# Premier ajout
print(f"{souffler.afficher_tache()}Agent recruté : Le grand méchant loup\n")
wolf_list.ajouter_tache(souffler)
print(wolf_list.affiche_liste())

# Test suppression
wolf_list.ajouter_tache(rouler)
print(wolf_list.affiche_liste())
wolf_list.supprimer_tache(rouler)
print(wolf_list.affiche_liste())

# Action du loup !
print("\nEt il souffla, souffla, souffla et la maison du petit cochon s'envola.")
wolf_list.marquer_comme_finie(souffler)

# tâches finies
print(wolf_list.filtrer_liste())
