class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur

    def get_largeur(self):
        return self.largeur

    def set_longueur(self, new_longueur):
        self.longueur = new_longueur

    def set_largueur(self,new_largeur):
        self.largeur = new_largeur

    def aire(self):
        air = (self.get_longueur() * self.get_largeur())
        print("l'aire est de : " + str(air))


rectangle = Rectangle(12, 4)
rectangle.aire()



