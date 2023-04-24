class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self,):
        add_result = self.nombre1 + self.nombre2
        print(str(self.nombre1) + "+" + str(self.nombre2) + "=" + str(add_result))


    def print_info(self):
        print("nombre 1 : " + str(self.nombre1))
        print("nombre 2 : " + str(self.nombre2))


operation = Operation(65, 20)
operation.print_info()
operation.addition()

# print(operation)


