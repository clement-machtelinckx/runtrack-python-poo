class Livre:
    def __init__(self):
        self.__disponible = True

    def get_disponible(self):
        return self.__disponible

    def set_disponible(self, dispo):
        self.__disponible = dispo

    def verification(self):
        if self.__disponible == True:
            print("livre dispo")
            return True
        elif self.__disponible == False:
            print("livre non dispo")
            return False
        # return self.__disponible


    def emprinter(self):
        if self.__disponible:
            self.__disponible = False
            print("livre emprunter avec succés")
            return True
        else:
            print("livre deja emprunter")
            return False

    def rendu(self):
        if not self.__disponible:
            self.__disponible = True
            print("livre rendu ")
        else:
            print("aucun livre a rendre")

livre = Livre()
livre.verification() # vérifie si le livre est dispo
livre.emprinter()
livre.rendu()

livre.set_disponible(False)
livre.verification()
livre.rendu()