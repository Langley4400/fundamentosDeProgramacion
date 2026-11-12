class Alumno:
    def __init__(self, nombre, promedio):
        self.nombre = nombre
        self.promedio = promedio

    def saludar(self):
        print ("Hola, soy", self.nombre)

a1 = Alumno("Ana", 9.2)
a2 = Alumno("Luis", 5.5)

a1.saludar()
a2.saludar()