'''
programa para estudiar los elementos del lenguaje de programación Python
mi nombre es miriel mariana herrera serrano 
'''
nombre = "Ana" #variable tipo string 
edad = 19 #variable tipo entero
estatura = 1.65 #variable tipo float
es_estudiante = True #variable tipo boolean

#imprimimos la variable y su tipo de dato
print ("Nombre:", nombre, type(nombre))
print ("Edad:", edad, type(edad))
print ("Estatura:", estatura, type(estatura))
print ("Es estudiante:", es_estudiante, type(es_estudiante))

#declaro una constante
PROMEDIO_MINIMO = 6
#introduccion de datos y los guardamos en variables materia y calificacion
materia = input("¿Que materia cursas?")
calificacion = float(input("¿Que calificacion tienes?"))

#hacemos las operaciones basicas
suma = 8 + 2
resta = 10 % 3
potencia = 2 ** 3

#estamos declarando dos variables tipo booleanas 
mayor_de_edad = edad >= 18
aprobado = calificacion >= PROMEDIO_MINIMO and es_estudiante

#imprimimos los resultados
print("Suma:", suma, "Resta:", resta, "Potencia:", potencia)
print("Mayor de edad:", mayor_de_edad)
