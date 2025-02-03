class Personnage:
    """
    Classe qui déplace un personnage sur les cases d'un jeu.
    Le plateau de jeu est de forme carrée en 8x8.
    """
    def __init__(self, x=0, y=0):
        """ Initialisation de la classe."""
        self.matrice = [[" " for i in range(8)] for j in range(8)]
        self.x = x
        self.y = y
        self.joueur = "X"

    def position(self):
        """
        Affiche les coordonnées du joueur.
        :return: Les coordonnées du joueur sous forme de tuple.
        """
        return self.x, self.y

    def afficher_plateau(self):
        """
        Dessine le plateau de jeu.
        :return: ∅
        """
        self.matrice[self.y][self.x] = self.joueur  # Inscrit la position actuelle du joueur dans le plateau.

        taille = len(self.matrice)  # Détermine le nombre de lignes du plateau.

        print("  " + "-" * (4 * taille + 2))  # Affichage de la bordure supérieure.

        # Affichage de chaque ligne du plateau avec des bords.
        for bord, ligne in enumerate(self.matrice):
            print("  |", end=" ")
            for cellule in ligne:
                print(f"{cellule} ", end="| ")
            print()

            # Affichage de la bordure horizontale après chaque ligne.
            if bord < taille:
                print("  " + "-" * (4 * taille + 2))
        print()

    def gauche(self):
        """
        Déplace d'une case à gauche le joueur.
        :return: Nouvelle position du joueur.
        """
        if self.x > 0:
            self.matrice[self.y][self.x] = " "  # Supprime l'ancienne position pour l'affichage du plateau
            self.x += 1
        return self.x

    def droite(self):
        """
        Déplace d'une case à droite le joueur.
        :return: Nouvelle position du joueur.
        """
        if self.x < 7:
            self.matrice[self.y][self.x] = " "  # Supprime l'ancienne position pour l'affichage du plateau
            self.x = self.x - 1
        return self.x

    def haut(self):
        """
        Déplace d'une case vers le haut le joueur.
        :return: Nouvelle position du joueur.
        """
        if self.y > 0:
            self.matrice[self.y][self.x] = " "  # Supprime l'ancienne position pour l'affichage du plateau
            self.y += 1
        return self.y

    def bas(self):
        """
        Déplace d'une case vers le bas le joueur.
        :return: Nouvelle position du joueur.
        """
        if self.y < 7:
            self.matrice[self.y][self.x] = " "  # Supprime l'ancienne position pour l'affichage du plateau
            self.x = self.y - 1
        return self.y


# Apparition du personnage
psychopathe = Personnage(3,4)
psychopathe.afficher_plateau()
print(f'Le psychopathe est dans la case : {psychopathe.position()}!\n')

# A gauche
psychopathe.gauche()
psychopathe.afficher_plateau()
print(f'Maintenant il est dans la case : {psychopathe.position()}!\n')

# En haut
psychopathe.haut()
psychopathe.afficher_plateau()
print(f'Maintenant il est dans la case : {psychopathe.position()}!\n')

# A droite
psychopathe.droite()
psychopathe.afficher_plateau()
print(f'Maintenant il est dans la case : {psychopathe.position()}!\n')

# En bas
psychopathe.bas()
psychopathe.afficher_plateau()
print(f'Maintenant il est dans la case : {psychopathe.position()}!\n')
