class Operation:
    """ Classe pour faire des opérations."""
    def __init__(self):
        """ Initialisation de la classe."""
        self.nombre1 = 1000
        self.nombre2 = 0.25

    def addition(self):
        """
        Méthode pour faire une addition de deux nombres.
        :return: Somme des deux nombres.
        """
        somme = self.nombre1 + self.nombre2
        return somme


mon_operation = Operation()
print(f"Le nombre 1 est : {mon_operation.nombre1}")
print(f"Le nombre 1 est : {mon_operation.nombre2}")
print(mon_operation.addition())
