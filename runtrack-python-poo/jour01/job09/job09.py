class Student:
    def __init__(self, nom, prenom, num_etudiant, credit=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__num_etudiant = num_etudiant
        self.__credit = credit


    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_num_etudiant(self):
        return self.__num_etudiant

    def get_credit(self):
        return self.__credit

    def set_nom(self, new_nom):
        self.__nom = new_nom

    def set_prenom(self, new_prenom):
        self.__prenom = new_prenom

    def set_num_etudiant(self, new_num_etudiant):
        self.__num_etudiant = new_num_etudiant

    def set_credit(self, new_credit):
        self.__credit = new_credit

    def add_credits(self, credit_added):
        if credit_added > 0:
            tt_credit = credit_added + self.get_credit()
            self.set_credit(tt_credit)

    def __student_eval(self, get_credit):
        if get_credit >= 90:
            return "Exellent"
        elif get_credit >= 80:
            return "Trés bien"
        elif get_credit >= 70:
            return"Bien"
        elif get_credit >= 60:
            return "Passable"
        elif get_credit < 60:
            return "Insufisant"


    def student_info(self, nom, prenom, num_etudiant, __student_eval):

        print("Nom = " + self.get_nom())
        print("Prénom = " + self.get_prenom())
        print("id = " + str(self.__num_etudiant))
        print("niveaux = " + self.__student_eval(student.get_credit()))



student = Student("Machtelinckx", "clément", 145)
student.add_credits(25)
student.add_credits(25)
student.add_credits(35)
print(student.get_credit())
print("le nombre de crédit de " + student.get_prenom() + " " + student.get_nom() + " etudiant " + str(student.get_num_etudiant()) + " est : " + str(student.get_credit()))
print("--------------------------------------------------")
student.student_info(student.get_nom(), student.get_prenom(), student.get_num_etudiant(), student.get_credit())
print("-----------------------------------------------")
#test method set

student.set_nom("Dupont")
student.set_prenom("Jean")
student.set_num_etudiant(246)
student.set_credit(90)
student.student_info(student.get_nom(), student.get_prenom(), student.get_num_etudiant(), student.get_credit())
print("--------------------------------")
#verif que la method set est prise en compte
print(student.get_nom())
print(student.get_prenom())
print(student.get_num_etudiant())
print(student.get_credit())
print("------------------------------")
