import random


class Estudiante:
    def __init__(self):
        self.nombre = input("Nombre del estudiante: ")
        self._edad = input("Edad del estudiante: ")
        self.__carnet = ''.join(str(random.randint(0, 9)) for _ in range(10))
        
        
    def nombre_getter(self):
        return self.nombre
    
    def edad_getter(self):
        return self._edad
    
    def carnet_getter(self):
        return self.__carnet
    
    def cambiar_carnet(self):
        self.__carnet = ''.join(str(random.randint(0, 9)) for _ in range(10))
        print(f"Su nuevo carnet: {self.__carnet}") 