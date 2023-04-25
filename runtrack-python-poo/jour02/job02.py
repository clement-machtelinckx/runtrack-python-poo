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
    def __init__(self):
        super().__init__()

    def aller_en_cour(self):
        print("je vait en cour")

    def affichage_age(self):
        print("jai 15 ans")

    """def bonjour(self):
        super().bonjour()
        print("hello")"""

class Professeur(Personne):
    def __init__(self, matiere_enseigner):
        self.__matiere_enseigner = matiere_enseigner
        super().__init__()

    def get_matiere_enseigner(self):
        return self.__matiere_enseigner

    def set_matiere_enseigner(self, new_matiere):
        self.__matiere_enseigner = new_matiere

    def enseigner(self):
        print("le cour va commencer")


personne = Personne(20)
personne.afficher_age()
eleve = Eleve()
eleve.afficher_age()
print("--------------------------------------")
eleve.bonjour()
eleve.aller_en_cour()
eleve.modifier_age(1)
eleve.afficher_age()
print("--------------------------------------")
#professeur test
professeur = Professeur("mathématique")
professeur.modifier_age(26)
professeur.afficher_age()
print(professeur.get_matiere_enseigner())
professeur.enseigner()


