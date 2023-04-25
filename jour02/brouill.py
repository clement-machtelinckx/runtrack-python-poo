import random


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur


    def get_valeur(self):
        return self.valeur

    def get_couleur(self):
        return self.couleur

    def set_valeur(self, new_valeur):
        self.valeur = new_valeur

    def set_couleur(self, new_couleur):
        self.couleur = new_couleur

class Jeu(Carte):
    def __init__(self):
        self.packet = []
        self.initialiser_packet()

    def get_packet(self):
        return self.packet

    def set_packet(self, new_packet):
        self.packet = new_packet

    def initialiser_packet(self):
        valeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, "V", "D", "R", "AS"]
        couleurs = ("coeur", "pique", "carreaux", "trefle")
        for valeur in valeurs:
            for couleur in couleurs:
                carte = Carte(valeur, couleur)
                self.packet.append(carte)

    def melanger(self):
        random.shuffle(self.packet)

    def distribuer(self, nb_carte):
        main = []
        for i in range(nb_carte):
            carte = random.choice(self.packet)
            main.append(carte)
            self.packet.remove(carte)
        return main

class Joueur:
    def __init__(self, main):
        self.main = main

    def get_main(self):
        return self.main

    def set_main(self, new_main):
        self.main = new_main

    def ajouter_carte(self, carte):
        self.main.append(carte)

    def retirer_carte(self, carte):
        self.main.remove(carte)

class Dealer:
    def __init__(self, main_deal):
        self.main_deal = main_deal

    def afficher_main(self):
        print(f"Main du dealer : [{self.main[0]}, *]")

    def get_main(self):
        return self.main

    def get_main_deal(self):
        return self.main_deal

    def set_main_deal(self, new_main_deal):
        self.main_deal = new_main_deal

    def ajouter_carte(self, carte):
        self.main_deal.append(carte)

    def retirer_carte(self, carte):
        self.main_deal.remove(carte)

class JeuBlackjack(Jeu):
    def __init__(self):
        super().__init__()

    def initialiser_packet(self):
        valeurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11]
        couleurs = ("coeur", "pique", "carreaux", "trefle")
        for valeur in valeurs:
            for couleur in couleurs:
                carte = Carte(valeur, couleur)
                self.packet.append(carte)

    def calculer_points(self, main):
        points = 0
        as_count = 0
        for carte in main:
            if carte.get_valeur() == 11:
                as_count += 1
            else:
                points += carte.get_valeur()
        while as_count > 0 and points + 11 > 21:
            points += 1
            as_count -= 1
        points += as_count * 11
        return points


def verif_valeur_main(main):
    valeur = 0
    as_count = 0
    for carte in main:
        if carte.get_valeur() == "AS":
            as_count += 1
        elif carte.get_valeur() in ["V", "D", "R"]:
            valeur += 10
        else:
            valeur += carte.get_valeur()

    for i in range(as_count):
        if valeur + 11 <= 21:
            valeur += 11
        else:
            valeur += 1
    return valeur

jeu = Jeu()
# Initialisation des joueurs et du dealer
joueur = Joueur(jeu.distribuer(2))
dealer = Dealer(jeu.distribuer(2))

# Fonction pour afficher les cartes d'un joueur
def afficher_main(joueur):
    main = joueur.get_main()
    for carte in main:
        print(carte.get_valeur(), carte.get_couleur())

# Fonction pour vérifier si un joueur a un blackjack (21 points avec 2 cartes)
def blackjack(joueur):
    main = joueur.get_main()
    if len(main) == 2 and verif_valeur_main(main) == 21:
        return True
    else:
        return False

# Déroulement du jeu
print("Main du joueur :")
afficher_main(joueur)

if blackjack(joueur):
    print("Blackjack !")
else:
    choix = input("Voulez-vous tirer une carte ? (o/n) ")
    while choix == "o":
        nouvelle_carte = jeu.distribuer(1)[0]
        joueur.ajouter_carte(nouvelle_carte)
        print("Main du joueur :")
        afficher_main(joueur)
        if verif_valeur_main(joueur.get_main()) > 21:
            print("Bust !")
            break
        choix = input("Voulez-vous tirer une carte ? (o/n) ")

if choix == "n":
    print("Main du dealer :")
    afficher_main(dealer)
    while verif_valeur_main(dealer.get_main()) < 17:
        nouvelle_carte = jeu.distribuer(1)[0]
        dealer.ajouter_carte(nouvelle_carte)
        print("Main du dealer :")
        afficher_main(dealer)
        if verif_valeur_main(dealer.get_main()) > 21:
            print("Dealer bust !")
            break

    # Comparaison des mains
    valeur_joueur = verif_valeur_main(joueur.get_main())
    valeur_dealer = verif_valeur_main(dealer.get_main())
    if valeur_joueur > 21:
        print("Vous avez perdu !")
    elif valeur_dealer > 21:
        print("Vous avez gagné !")
    elif valeur_joueur > valeur_dealer:
        print("Vous avez gagné !")
    elif valeur_dealer > valeur_joueur:
        print("Vous avez perdu !")
    else:
        print("Égalité !")

print("Fin de la partie.")


