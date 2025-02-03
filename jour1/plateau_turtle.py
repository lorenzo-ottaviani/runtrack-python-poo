import turtle


class Plateau:
    def __init__(self, x, y):
        """ Initialisation de la classe."""
        self.matrice = [[" " for i in range(8)] for j in range(8)]  # Crée un plateau de 8x8
        self.x = x  # Position initiale du joueur sur x
        self.y = y  # Position initiale du joueur sur y
        self.turtle = turtle.Turtle()  # Crée une instance de turtle
        self.screen = turtle.Screen()  # Crée un écran turtle
        self.screen.setup(width=600, height=600)  # Taille de l'écran turtle
        self.turtle.speed(0)  # On définit la vitesse maximale pour dessiner rapidement

    def position(self):
        """
        Affiche les coordonnées du joueur.
        :return: Les coordonnées du joueur sous forme de tuple.
        """
        return self.x, self.y

    def dessiner_case(self, x, y, taille=50):
        """
        Dessine une case à la position (x, y).
        :param x: Coordonnée x pour placer la case.
        :param y: Coordonnée y pour placer la case.
        :param taille: La taille de chaque case (par défaut 50).
        """
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        for _ in range(4):
            self.turtle.forward(taille)
            self.turtle.right(90)

    def colorier_case(self, x, y, taille=50, couleur="black"):
        """
        Colorie la case du joueur à la position (x, y) en noir.
        :param x: Coordonnée x pour placer la case.
        :param y: Coordonnée y pour placer la case.
        :param taille: La taille de chaque case (par défaut 50).
        :param couleur: La couleur de la case à remplir (par défaut "black").
        """
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        self.turtle.begin_fill()  # Démarrer le remplissage
        self.turtle.fillcolor(couleur)  # Définir la couleur de remplissage
        for _ in range(4):
            self.turtle.forward(taille)
            self.turtle.right(90)
        self.turtle.end_fill()  # Terminer le remplissage

    def afficher_plateau(self):
        """
        Affiche le plateau de jeu à l'aide de Turtle.
        """
        taille_case = 50  # Taille de chaque case
        start_x = -200  # Position initiale x
        start_y = 200  # Position initiale y

        # Dessiner les cases
        for i in range(8):
            for j in range(8):
                self.dessiner_case(start_x + j * taille_case, start_y - i * taille_case, taille_case)

        # Colorier la case du joueur en noir
        joueur_x_pos = start_x + self.y * taille_case
        joueur_y_pos = start_y - self.x * taille_case

        self.colorier_case(joueur_x_pos, joueur_y_pos, taille_case, couleur="black")

        # Cacher la tortue après avoir dessiné le plateau
        self.turtle.hideturtle()


# Exemple d'utilisation
plateau = Plateau(3, 4)  # Le joueur commence à la position (3, 4)
plateau.afficher_plateau()

# Garder la fenêtre ouverte jusqu'à ce qu'on la ferme manuellement
turtle.done()
