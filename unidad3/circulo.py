import math

radio = float(input("Radio del Circulo: "))
area = math.pi * math.pow(radio, 2)
perimetro = 2 * math.pi * radio

print("Area: ", round(area, 2))
print("Perimetro: ", round(perimetro, 2))
print("Raiz cuadrada del radio: ", round(math.sqrt(radio), 2))
print("techo del radio: ", round(math.ceil(area)))

'''Explicar como funciona la linea 1: import math. 
tambien seleccione dos operaciones de la libreria math y ejecutelas'''

x= 3
y= 2 
pow = math.pow(x,y)
print("x , y: ", pow)

x= 16
y= 4 
log = math.log(x,y)
print(" x , y: ", log)
