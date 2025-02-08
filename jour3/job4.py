class Joueur:
    """ Classe qui gère des joueurs de foot. """

    def __init__(self, nom, numero, position, nombre_buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        """
        Initialisation de la classe.
        :param nom: Nom du joueur.
        :param numero: Son numéro.
        :param position: Sa position sur le terrain.
        :param nombre_buts: Son nombre de buts marqués.
        :param passes_decisives: Son nombre de passes décisives.
        :param cartons_jaunes: Son nombre de cartons jaunes.
        :param cartons_rouges: Son nombre de cartons rouges.
        """
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nombre_buts = nombre_buts
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquer_but(self):
        """
        Permet d'ajouter un but au nombre de buts marqués par le joueur.
        :return: ∅
        """
        self.nombre_buts += 1

    def effectuer_passe_decisive(self):
        """
        Ajoute une passe décisive aux statistiques du joueur.
        :return: ∅
        """
        self.passes_decisives += 1

    def recevoir_carton_jaune(self):
        """
        Ajoute un carton jaune aux statistiques du joueur.
        :return: ∅
        """
        self.cartons_jaunes += 1

    def recevoir_carton_rouge(self):
        """
        Ajoute un carton rouge aux statistiques du joueur.
        :return: ∅
        """
        self.cartons_rouges += 1

    def afficher_statistiques(self):
        """
        Affiche les statistiques du joueur.
        :return: Ses statistiques.
        """
        stats = (f"{self.nom}\nJoue comme {self.position} avec le maillot n°{self.numero}.\nNombre de buts marqués : "
                 f"{self.nombre_buts}\nNombre de passes décisives : {self.passes_decisives}\nNombre de cartons jaunes :"
                 f" {self.cartons_jaunes}\nNombre de cartons rouges : {self.cartons_rouges}\n")
        return stats


class Equipe:
    """Classe qui gère une équipe de foot. """

    def __init__(self, nom):
        """
        Initialisation de la classe.
        :param nom: Nom de l'équipe.
        """
        self.nom = nom
        self.liste_joueurs = []

    def ajouter_joueur(self, joueur):
        """
        Ajoute un joueur à la liste des joueurs.
        :param joueur: Un objet de la classe Joueur.
        :return: ∅
        """
        self.liste_joueurs.append(joueur)

    def afficher_statistiques_joueurs(self):
        """
        Affiche les statistiques de chacun des joueurs de l'équipe.
        :return: Les statistiques.
        """
        for joueur in self.liste_joueurs:
            print(joueur.afficher_statistiques())

    def mettre_a_jour_statistiques_joueur(self, joueur_mis_a_jour):
        """
        Mets à jour les statistiques d'un des joueurs.
        :param joueur_mis_a_jour: Les statistiques du joueur mises à jour.
        :return: ∅
        """
        for i, joueur in enumerate(self.liste_joueurs):
            if joueur.nom == joueur_mis_a_jour.nom:
                self.liste_joueurs[i] = joueur_mis_a_jour


# Création de l'équipe 1 : les chats

Felix = Joueur("Felix", 1, "Gardien")
Tom = Joueur("Tom", 2, "Défenseur")
Garfield = Joueur("Garfield", 9, "Attaquant")
Simba = Joueur("Simba", 4, "Défenseur")
Cheshire = Joueur("Cheshire", 8, "Milieu")
Bagheera = Joueur("Bagheera", 5, "Défenseur")
Puss = Joueur("Puss", 11, "Attaquant")
Salem = Joueur("Salem", 6, "Milieu")
Catwoman = Joueur("Catwoman", 3, "Défenseur")
Heathcliff = Joueur("Heathcliff", 7, "Milieu")
Mufasa = Joueur("Mufasa", 10, "Attaquant")

chats = Equipe("Les chats")
chats.ajouter_joueur(Felix)
chats.ajouter_joueur(Tom)
chats.ajouter_joueur(Garfield)
chats.ajouter_joueur(Simba)
chats.ajouter_joueur(Cheshire)
chats.ajouter_joueur(Bagheera)
chats.ajouter_joueur(Puss)
chats.ajouter_joueur(Salem)
chats.ajouter_joueur(Catwoman)
chats.ajouter_joueur(Heathcliff)
chats.ajouter_joueur(Mufasa)

# Affichage des statistiques de l'équipe des chats
print("Statistiques des joueurs de l'équipe des chats :")
chats.afficher_statistiques_joueurs()


# Création de l'équipe 2 : les chiens

Pluto = Joueur("Pluto", 1, "Gardien")
Snoopy = Joueur("Snoopy", 2, "Défenseur")
Scooby_Doo = Joueur("Scooby-Doo", 9, "Attaquant")
Brian = Joueur("Brian", 4, "Défenseur")
Laika = Joueur("Laïka", 8, "Milieu")
Rin_Tin_Tin = Joueur("Rin-Tin-Tin", 5, "Défenseur")
Spunky = Joueur("Spunky", 11, "Attaquant")
Scooby = Joueur("Scooby", 6, "Milieu")
Toto = Joueur("Toto", 3, "Défenseur")
Odie = Joueur("Odie", 7, "Attaquant")
Hachi = Joueur("Hachi", 10, "Milieu")


chiens = Equipe("Les chiens")
chiens.ajouter_joueur(Pluto)
chiens.ajouter_joueur(Snoopy)
chiens.ajouter_joueur(Scooby_Doo)
chiens.ajouter_joueur(Brian)
chiens.ajouter_joueur(Laika)
chiens.ajouter_joueur(Rin_Tin_Tin)
chiens.ajouter_joueur(Spunky)
chiens.ajouter_joueur(Scooby)
chiens.ajouter_joueur(Toto)
chiens.ajouter_joueur(Odie)
chiens.ajouter_joueur(Hachi)

# Affichage des statistiques de l'équipe des chiens
print("Statistiques des joueurs de l'équipe des chiens :")
chiens.afficher_statistiques_joueurs()

# Lancement du match
print(f"Bonjour! Le match va bientôt commencer!\nLa première équipe est {chats.nom} elle porte le maillot vert,"
      f" la seconde est {chiens.nom} elle porte le maillot rouge.\nLe match va commencer!\n")

# 1ère mi-temps

print("10ème minute. Garfield fait une passe décisive pour Heathcliff, qui marque ! Les chats mènent 1-0.")
Garfield.effectuer_passe_decisive()
chats.mettre_a_jour_statistiques_joueur(Garfield)
Heathcliff.marquer_but()
chats.mettre_a_jour_statistiques_joueur(Heathcliff)

print("14ème minute. Scooby-Doo tente une frappe à distance mais Felix, le gardien des chats, arrête le tir.")

print("22ème minute. Carton jaune pour Snoopy après un tacle dur sur Mufasa.")
Snoopy.recevoir_carton_jaune()
chiens.mettre_a_jour_statistiques_joueur(Snoopy)

print("30ème minute. Tom intercepte le ballon et l’envoie à Puss, qui marque dans un superbe contre !"
      " Les chats mènent 2-0.")
Puss.marquer_but()
chats.mettre_a_jour_statistiques_joueur(Puss)

print("35ème minute. Carton jaune pour Simba suite à une obstruction sur Odie.")
Simba.recevoir_carton_jaune()
chats.mettre_a_jour_statistiques_joueur(Simba)

print("40ème minute. Mufasa effectue une passe à Garfield qui marque un superbe but ! Les chats mènent désormais 3-0.")
Mufasa.effectuer_passe_decisive()
chats.mettre_a_jour_statistiques_joueur(Mufasa)
Garfield.marquer_but()
chats.mettre_a_jour_statistiques_joueur(Garfield)

print("45ème minute. Carton jaune pour Spunky après une faute sur Catwoman. La première mi-temps se termine.")
Spunky.recevoir_carton_jaune()
chiens.mettre_a_jour_statistiques_joueur(Spunky)

# Mi-temps
print("\nMi-temps ! Les chats mènent 3-0. Les chiens vont devoir se réveiller pour la seconde mi-temps.\n")

# 2ème mi-temps

print("50ème minute. Scooby-Doo marque pour les chiens après une belle passe de Laïka. Le score est maintenant 3-1.")
Laika.effectuer_passe_decisive()
chats.mettre_a_jour_statistiques_joueur(Laika)
Scooby_Doo.marquer_but()
chiens.mettre_a_jour_statistiques_joueur(Scooby_Doo)

print("57ème minute. Quel incident ! Un des chiens mord un chat ! Carton rouge pour Rin-Tin-Tin, qui est expulsé !")
Rin_Tin_Tin.recevoir_carton_rouge()
chiens.mettre_a_jour_statistiques_joueur(Rin_Tin_Tin)

print("63ème minute. Les chats profitent de l’avantage numérique, et Heathcliff marque son deuxième but !"
      " 4-1 pour les chats.")
Heathcliff.marquer_but()
chats.mettre_a_jour_statistiques_joueur(Heathcliff)

print("70ème minute. Odie réduit l'écart avec un tir puissant qui bat Felix ! Le score est maintenant 4-2.")
Odie.marquer_but()
chiens.mettre_a_jour_statistiques_joueur(Odie)

print("75ème minute. Carton jaune pour Laïka suite à un contact un peu trop musclé avec Bagheera.")
Laika.recevoir_carton_jaune()
chiens.mettre_a_jour_statistiques_joueur(Laika)

print("80ème minute. Les chats se défendent bien, et la pression des chiens ne parvient pas à percer la défense.")

print("85ème minute. Carton jaune pour Puss après un tirage de maillot sur Scooby.")
Puss.recevoir_carton_jaune()
chats.mettre_a_jour_statistiques_joueur(Puss)

print("90ème minute. Le match se termine sur le score de 4-2 pour les chats ! Quelle victoire !")

# Fin du match
print(f"\nLe match est terminé ! {chats.nom} s’impose 4-2 contre {chiens.nom} ! Félicitations aux vainqueurs !")

# Affichage des statistiques des joueurs après le match
print("\nStatistiques des joueurs de l'équipe des chats :")
chats.afficher_statistiques_joueurs()

print("\nStatistiques des joueurs de l'équipe des chiens :")
chiens.afficher_statistiques_joueurs()
