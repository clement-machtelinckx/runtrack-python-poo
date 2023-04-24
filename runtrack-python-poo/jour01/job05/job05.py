class Animal:

    def __init__(self):
        self.age = 0
        self.nom = ""

    def vieillir(self):
        self.age += 1
        # print(self.nom + " " + str(self.age))

    def nomer(self):
        self.nom = "chien"

animal = Animal()
print("age initial " + str(animal.age))
animal.vieillir()
print("age aprés viellisement " + str(animal.age))
animal.nomer()
print("le nom de l'annimal est : " + animal.nom)

