import math
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

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def aire(self):
        air_cercle = ((self.get_radius()**2) * (math.pi))
        print("l'aire du cercle est de : " + str(air_cercle))



rectangle = Rectangle(12, 4)
rectangle.aire()
cercle = Cercle(6)
cercle.aire()
