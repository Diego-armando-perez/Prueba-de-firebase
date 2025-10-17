# Prueba-de-firebase
Algo pequeño que pone a prueba las cuatro funciones principales de firebse

📋 Descripción
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
El repositorio contiene 3 carpetas las cuales forman juntas una pequeña practica que prueba las 4 opciones que otorga firebase para manejo de bases de datos, Crear un dato, modificar un dato, leer un dato y elimiar un dato
para este pequeño ejemplo se usa el caso de uso de un estudiante registrandose en una pagina universitaria

🖋️ Contenido
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
El trabajo trae tres carpetas, las carpetas se llaman:
"Data", "Ejemplo", "Main"

Que hace cada carpeta? Las carpetas "Data" y "Ejemplo" traen lo que son clases con metodos las cuales se relacionan en "Main" para hacer funcionar el codigo

<img width="790" height="515" alt="image" src="https://github.com/user-attachments/assets/8efaa001-0838-4bb8-a131-a27d936de9fd" />

Aqui es observable el codigo de "main" en el cual se importan ambas carpetas "Data" y "Ejemplo"

"Data" y "Ejemplo" Como se ha mencionado traen una clase cada una, "Data" Trae la clase de firebase que hace funcionar todo lo relacionado a los servidores en tiempo real y "Ejemplo" contiene toda la informacion y acciones que puede realizar el estudiante

<img width="1047" height="607" alt="image" src="https://github.com/user-attachments/assets/b047e131-ed31-40cd-94c4-5810ca806509" />

<img width="895" height="698" alt="image" src="https://github.com/user-attachments/assets/6b075d99-2c9b-4254-9e6b-b0f49020c6b8" />

🛠️ Tecnologías Utilizadas
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Visual studio code
Python 3.15
Firebase

🔧 Configuración y Instalación
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
No es posible usar el archivo original, pero si se le aplica un archivo propio de firebase entonces el programa correra perfectamente en su computador, para hacerlo funcionar porfavor descarge el archivo y dirigase a data alli encontrara dos cosas importantes, cred y databaseURL, con estos dos porfavor remplaze el directorio que aparece en cred con el que usted tenga su clave privada y databaseURL con el link de su projecto, como no es posible otorgar el acceso sin riesgo a los archivos que fueron usados por mi estas dos cosas deben ser cambiadas por informacion propia del usuario, una vez hecho esto tambien asegurese de instalar con pip, firebase-admin y firebase, despues de todos estos pasos le deberia de ser posible observar los valores cambiando y registrandose en su pagina de servidor de firebase cuando el programa se ejecute

🔧 Uso de la aplicacion
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Descarge todas las carpetas y cambie la informacion mencionada en la seccion de configuracion, una vez hecho esto corra el codigo del main y compruebe con firebase, vera que cuando se corra el main primero se creara un estudiante en forma de objeto 

<img width="340" height="65" alt="image" src="https://github.com/user-attachments/assets/f74f2737-83b5-4e8c-9046-9d3b81cfd820" />

Este estudiante preguntara por un nombre y una edad

<img width="356" height="81" alt="image" src="https://github.com/user-attachments/assets/0f68d2aa-2bed-40a8-8758-5e384ea2873e" />

Y una vez ingresados generara un carnet el cual contendra una secuencia aleatoria de 10 numeros. Ahora aqui viene lo especial de firebase
Lo primero que se hara con el programa es el crear un dato bajo el directorio estudiantes donde la informacion del alumno se guardara

<img width="459" height="284" alt="image" src="https://github.com/user-attachments/assets/59d8dcbc-077b-4d4e-bdc5-abc0c7e04c95" />

Aqui se hara uso de la primera funcion que nos otorga firebase la cual es la de creación, pero al mismo tiempo se uso la de cambio, lo que ocurre esque en la secuencia que da el main el programa crea al estudiante pero tambien le cambia su carnet esto es observable por medio de la consola y codigo

<img width="498" height="145" alt="image" src="https://github.com/user-attachments/assets/0518b4a5-3ca0-45d6-9e4c-6df53bf96897" />
<img width="313" height="85" alt="image" src="https://github.com/user-attachments/assets/af0b8c46-3085-4bfe-86ba-314f616e70f7" />
