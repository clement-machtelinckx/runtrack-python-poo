class Voiture:
    def __init__(self, marque, model, annee, kilometrage, reservoir=50, en_marche=False):
        self.__marque = marque
        self.__model = model
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def get_model(self):
        return self.__model

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, new_reservoir):
        self.__reservoir = new_reservoir

    def set_marque(self, new_marque):
        self.__marque = new_marque

    def set_model(self, new_model):
        self.__model = new_model

    def set_annee(self, new_annee):
        self.__annee = new_annee

    def set_kilometrage(self, new_kilometrage):
        self.__kilometrage = new_kilometrage

    def set_en_marche(self, new_marche):
        self.__en_marche = new_marche


    def demarrer(self):
        if self.get_en_marche() == False and self.__verifier_plein() >= 5:
            self.set_en_marche(True)
        else:
            pass

    def arreter(self):
        if self.get_en_marche() == True:
            self.set_en_marche(False)
        else:
            pass

    def __verifier_plein(self):
        return self.get_reservoir()


voiture = Voiture("Ferrari", "KiVaVit", 2010, 25000)

# Test des méthodes de getter
print("Marque :", voiture.get_marque())
print("Modèle :", voiture.get_model())
print("Année :", voiture.get_annee())
print("Kilométrage :", voiture.get_kilometrage())
print("En marche :", voiture.get_en_marche())
print("Niveau de réservoir :", voiture.get_reservoir())
print("------------------------------------------------")
# Test des méthodes de setter
voiture.set_reservoir(30)
voiture.set_marque("Lamborghini")
voiture.set_model("Huracan")
voiture.set_annee(2020)
voiture.set_kilometrage(5000)
voiture.set_en_marche(True)
voiture.set_en_marche(False)

#test apré modif

print("Marque :", voiture.get_marque())
print("Modèle :", voiture.get_model())
print("Année :", voiture.get_annee())
print("Kilométrage :", voiture.get_kilometrage())
print("Niveau de réservoir :", voiture.get_reservoir())

print("---------------------------------------------------")
# Test des méthodes demarrer et arreter
voiture.demarrer()
print("demarrer :", voiture.get_en_marche())
voiture.arreter()
print("arreter :", voiture.get_en_marche())

# test reservoir < 5
voiture.set_reservoir(4)
voiture.demarrer()
print("voiture pas asser d'essence")
print("try demarrer :", voiture.get_en_marche())
