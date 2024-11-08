print(" ")
print("Ordonez Martinez Valeria")
print(" ")

nombre =str(input("Ingrese el nombre: "))  #Solicitar nombre
apellido=str(input("Ingresa el apellido: "))  #Solicitar apellido
print(" ")


if nombre != "Daniel": #Agregar condicion si el nombre es incorrecto
    print("El nombre no es correcto") #imprimir mensaje
elif apellido != "Ramos": #Agregar  condicion si el apellido es incorrecto
    print("El apellido no es correcto") #Imprimir mensaje
else:
    print ("El nombre es: ", nombre, apellido) # se imprime el nombre
print (" ")



