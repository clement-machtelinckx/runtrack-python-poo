import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return "{} de {}".format(self.valeur, self.couleur)

class Jeu:
    def __init__(self):
        self.paquet = []
        couleurs = ["Coeur", "Carreau", "Trèfle", "Pique"]
        for couleur in couleurs:
            for valeur in range(2, 11):
                self.paquet.append(Carte(str(valeur), couleur))
            for valeur in ["Valet", "Dame", "Roi"]:
                self.paquet.append(Carte(valeur, couleur))
            self.paquet.append(Carte("As", couleur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.main = []

    def recevoir_carte(self, carte):
        self.main.append(carte)

    def calculer_score(self):
        score = 0
        as_compte = 0
        for carte in self.main:
            if carte.valeur == "As":
                as_compte += 1
            elif carte.valeur in ["Valet", "Dame", "Roi"]:
                score += 10
            else:
                score += int(carte.valeur)
        for i in range(as_compte):
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        return score

    def afficher_main(self):
        print("{} a en main :".format(self.nom))
        for carte in self.main:
            print("   ", carte)

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger()
        self.joueur = Joueur("Joueur")
        self.croupier = Joueur("Croupier")

    def jouer(self):
        print("Début du jeu")
        self.joueur.recevoir_carte(self.jeu.tirer_carte())
        self.croupier.recevoir_carte(self.jeu.tirer_carte())
        self.joueur.recevoir_carte(self.jeu.tirer_carte())
        self.croupier.recevoir_carte(self.jeu.tirer_carte())

        self.joueur.afficher_main()
        while True:
            choix = input("Voulez-vous prendre une carte ? (o/n) ")
            if choix.lower() == "o":
                self.joueur.recevoir_carte(self.jeu.tirer_carte())
                self.joueur.afficher_main()
                if self.joueur.calculer_score() > 21:
                    print("Vous avez perdu !")
                    return
            else:
                break

        score_joueur = self.joueur.calculer_score()
        print("Le score du joueur est :", score_joueur)

        score_croupier = self.croupier.calculer_score()
        while score_croupier < 17:
            self.croupier.recevoir_carte(self.jeu.tirer_carte())
            score_croupier = self.croupier.calculer_score()

        print("Le score du croupier est :", score_croupier)

        if score_joueur > 21 and score_croupier <21:
            print("Vous avez perdu !")
        elif score_joueur > score_croupier:
            print("Vous avez gagné !")
        elif score_joueur == score_croupier:
            print("Match nul !")
        elif score_croupier >21:
            print("Vous avez gagner, le croupier a trop piocher")
        else:
            print("Le croupier a gagné !")


blackjack = Blackjack()
blackjack.jouer()