class Veicule:
    def __init__(self, marque, model, annee, prix):
        self.marque = marque
        self.model = model
        self.annee = annee
        self.prix = prix

    def get_marque(self):
        return self.marque

    def get_model(self):
        return self.model

    def get_annee(self):
        return self.annee

    def get_prix(self):
        return self.prix

    def set_marque(self, new_marque):
        self.marque = new_marque

    def set_model(self, new_model):
        self.model = new_model

    def set_annee(self, new_annee):
        self.annee = new_annee

    def set_prix(self, new_prix):
        self.prix = new_prix

    def demarrer(self):
        print("je demarre mon veicule.")
    def information_veicule(self):
        print("marque : " + self.marque)
        print("model : " + self.model)
        print("annee : " + str(self.annee))
        print("prix : " + str(self.prix))


class Voiture(Veicule):
    def __init__(self, marque, model, annee, prix, porte=4):
        super().__init__(marque, model, annee, prix)
        self.porte = porte


    def get_porte(self):
        return self.porte

    def set_porte(self, new_porte):
        self.porte = new_porte

    def demarrer(self):
        print("je demarre ma voiture.")
    def information_veicule(self):
        print("marque : " + self.marque)
        print("model : " + self.model)
        print("nb de porte : " + str(self.porte))
        print("annee : " + str(self.annee))
        print("prix : " + str(self.prix))

class Moto(Veicule):
    def __init__(self, marque, model, annee, prix, roue =2):
        super().__init__(marque, model, annee, prix)
        self.roue = roue


    def demarrer(self):
        print("je demarre ma moto.")

    def information_veicule(self):
        print("marque : " + self.marque)
        print("model : " + self.model)
        print("annee : " + str(self.annee))
        print("prix : " + str(self.prix))
        print("nb de roue : " + str(self.roue))



veicule = Veicule("ferrari","KiVaVit", 2010, 250000)
veicule.demarrer()
veicule.information_veicule()
print("-------------------")

voiture = Voiture("Mercedes", "Classe A", 1850, 2020)
voiture.demarrer()
voiture.information_veicule()
print("---------------------------")

moto = Moto("Yamaha", "1200 Vmax", 4500, 1987)
moto.demarrer()
moto.information_veicule()