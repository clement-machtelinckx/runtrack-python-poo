class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur

    def set_largeur(self, new_largueur):
        self.__largeur = new_largueur



    def perimetre(self):
        peri =(self.get_longueur()*2) + (self.get_largeur()*2)
        print("le périmètre est de : " + str(peri))

    def surface(self):
        surf = self.get_longueur() * self.get_largeur()
        print("la surface est de : " + str(surf))

class Parallepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def get_hauteur(self):
        return self.hauteur

    def set_hauteur(self, new_hauteur):
        self.hauteur = new_hauteur

    def volume(self):
        vol = self.get_longueur() * self.get_largeur() * self.hauteur
        print("le volume est de : " + str(vol))




rectangle = Rectangle(12, 7)

rectangle.perimetre()
rectangle.surface()

print("------------------")
parallepipede = Parallepipede(12, 8, 5)
parallepipede.perimetre()
parallepipede.surface()
parallepipede.volume()
