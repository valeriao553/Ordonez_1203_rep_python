print(" ")
print(" Ordonez Martinez Valeria")
print(" ")


def nota(calif): #Definir la nota con la calificacion y regresar mensaje
    if calif <= 5: #Agregar condicion
        return "SUSPENSO"  #regresar mensaje
    elif calif <=6: #Agregar condicion
        return "SUFICIENTE"  #regresar mensaje
    elif calif <=7:  #Agregar condicion
        return "BIEN"  #regresar mensaje
    elif calif <=8:  #Agregar condicion
        return "NOTABLE"  #regresar mensaje
    elif calif <=9 <=10:  #Agregar condicion
        return "SOBRESALIENTE"  #regresar mensaje
    else:
        print("NOTA NO VALIDA")  


calif=int(input("Ingresa tu calificacion: "))  #Solicitar la calificacion
print(" ")
mensaje= nota(calif)  #Declarar variavle
print(mensaje) #Imprimir la variable del mensaje
print(" ")
            

