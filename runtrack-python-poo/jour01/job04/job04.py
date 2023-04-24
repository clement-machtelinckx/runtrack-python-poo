class Person:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom


    def se_presenter(self):
        # nom = input("entrez votre nom : ")
        # prenom = input("rentrez votre prenom : ")
        print("Bonjour " + self.nom + " " + self.prenom)

person1 = Person("machtelinckx", "clement")
person1.se_presenter()
person2 = Person("La tulipe", "fanfan")
person2.se_presenter()