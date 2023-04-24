class Operation:

    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def print_info(self):
        print("nombre 1 : " + str(self.nombre1))
        print("nombre 2 : " + str(self.nombre2))


operation = Operation(12, 3)
operation.print_info()

# print(operation)



