import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate(r"C:\Users\perez\Downloads\Prueba de firebase crud\Data\prueba-firebase-f0201-firebase-adminsdk-fbsvc-d5d3cee0d2.json")
firebase_admin.initialize_app(cred, {"databaseURL" : "https://prueba-firebase-f0201-default-rtdb.firebaseio.com/"})

class Firebasecontrol:
    def __init__(self):
        self.ref = db.reference("/estudiantes")
        
    def crear(self, estudiante):
        self.ref = db.reference("/estudiantes")
        self.nuevo = self.ref.child(str(estudiante.nombre_getter())).set(
        {
            "2 edad" : f"{estudiante.edad_getter()}",
            "3 carnet" : f"{estudiante.carnet_getter()}",
            "1 nombre" : f"{estudiante.nombre_getter()}"
        }
        )
        
    def cambiar_carnet(self, estudiante):
        self.ref = db.reference("/estudiantes" + f"/{estudiante.nombre_getter()}")
        self.cambio = self.ref.update(
        {
            "3 carnet" : f"{estudiante.carnet_getter()}"
        }    
        )
        
    def leer_dato(self, estudiante):
        self.ref = db.reference("/estudiantes" + f"/{estudiante.nombre_getter()}")
        self.lectura = self.ref.get()
        print (f"{estudiante.nombre_getter()}: ", self.lectura)
        
    def eliminar(self, estudiante):
        self.ref = db.reference("/estudiantes" + f"/{estudiante.nombre_getter()}")
        self.borrar = self.ref.delete()
        print ("El estudiante ha sido eliminado de la base de datos exitosamente")