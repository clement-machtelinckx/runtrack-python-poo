class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        print("longueur " + str(self.__longueur) + " largeur " + str(self.__largeur))

    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur

    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

rectangle = Rectangle(10, 5)
print(rectangle)
rectangle.set_longueur(20)
rectangle.set_largeur(10)
print(rectangle.get_longueur())
print(rectangle.get_largeur())

# print(rectangle.get_longueur() * rectangle.get_largeur())



