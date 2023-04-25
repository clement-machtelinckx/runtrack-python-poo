class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficher_age(self):
        print(self.age)

    def bonjour(self):
        print("hello")

    def modifier_age(self, add_age):
        self.age = self.age + add_age

class Eleve(Personne):

    def aller_en_cour(self):
        print("je vait en cour")

    def affichage_age(self):
        print("jai 15 ans")


class Professeur:
    def __init__(self, matiere_enseigner):
        self.__matiere_enseigner = matiere_enseigner

    def get_matiere_enseigner(self):
        return self.__matiere_enseigner

    def set_matiere_enseigner(self, new_matiere):
        self.__matiere_enseigner = new_matiere

    def enseigner(self):
        print("le cour va commencer")


personne = Personne()
personne.afficher_age()
eleve = Eleve()
eleve.afficher_age()