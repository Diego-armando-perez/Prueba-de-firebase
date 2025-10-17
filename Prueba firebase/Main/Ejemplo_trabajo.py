import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Data.Prueba_firebase_crud import Firebasecontrol
from Ejemplo.Clase import Estudiante

def main():
    estudiante1 = Estudiante()
    print(f"{estudiante1.carnet_getter()}")
    storage = Firebasecontrol()
    storage.crear(estudiante1)
    estudiante1.cambiar_carnet()
    storage.cambiar_carnet(estudiante1)
    storage.leer_dato(estudiante1)
    storage.eliminar(estudiante1)
    

if __name__ == "__main__":
    main()