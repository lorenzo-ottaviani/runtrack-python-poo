class Animal:
    """ Classe qui donne des informations sur des animaux."""

    def __init__(self):
        """ Initialisation de la classe."""
        self.espece = ""
        self.age = 0

    def vieillir(self):
        """
        Fait vieillir l'animal d'un an.
        :return: Le nouvel âge de l'animal.
        """
        self.age += 1
        return self.age

    def nommer(self, espece):
        """
        Affecte une espèce à l'animal.
        :return: L'espèce de l'animal.
        """
        self.espece = espece
        return self.espece


Thon = Animal()
print(f"J'ai {Thon.age} ans!")
print(f"Mon espèce est {Thon.nommer("thon")}.")
for annees in range(10):
    Thon.vieillir()
    if Thon.age == 1:
        print(f"J'ai grandi! Maintenant, j'ai {Thon.age} an!")
    elif Thon.age == 10:
        print(f"Je suis mort! J'étais trop vieux!! J'aurai eu {Thon.age} ans!")
    else:
        print(f"J'ai encore vieilli!! Maintenant, j'ai {Thon.age} ans!")
    annees += 1

