class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages


    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return int(self.__nb_pages)


    def set_titre(self, new_titre):
        self.__titre = new_titre

    def set_auteur(self, new_auteur):
        self.__auteur = new_auteur

    def set_nb_pages(self, new_nb_pages):
        if self.get_nb_pages() > 0:
            self.__nb_pages = new_nb_pages
        else:
            print("erreur nombre de page négatif")





livre = Livre("Le petit prince", "the pilot", 100)
# info avant modif
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nb_pages())
# modif livre

livre.set_titre("harry potter")
livre.set_auteur("JKR")
livre.set_nb_pages(370) # nombre de page possitif

#afficher le resultat des modif
print(livre.get_titre())
print(livre.get_auteur())
print(livre.get_nb_pages())

# livre.set_nb_pages(-10) # nombre de page negatif pour test
# print(livre.get_nb_pages())
