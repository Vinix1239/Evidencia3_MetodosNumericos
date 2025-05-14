#Metodo de Gauss
#Pedirle al usuario numeros para crear una matriz
matriz = []
print("Hola :>")
print("Ingresa 12 numeros para crear una matriz de 3x4")
for i in range(3):
    fila = []
    for j in range(4):
        elemento = float(input("numero: "))
        fila.append(elemento)
    matriz.append(fila)
renglon = 0

#Bucle para poder iterar sobre cada fila de la matriz
for i in range (renglon, renglon < 3, renglon= renglon+1):
    
    #Se selecciona el elemento que esta en diagonal como pivote
    pivote = matriz[renglon, renglon]

    #Aqui se va a normalizar el renglón dividiendo cada elemento por el pivote
    columna = 0
    for i in range(columna, columna < 4, columna = columna + 1):
        matriz[renglon, columna] = matriz[renglon, columna]/pivote

    #Aqui se va a eliminar los elementos que estan en la misma columna que el pivote seleccionado
    renglon_eliminado = 0
    for i in range(renglon_eliminado, renglon_eliminado < 3, renglon_eliminado= + 1):
        #Se verifica si el renglon actual no es el mismo que el se esta procesando
        if renglon_eliminado != renglon:
            #Se selecciona el factor por el que se va a multiplicar el renglon principal para poder eliminar el elemento
            factor = matriz[renglon_eliminado, renglon]

            #Se resta el renglón principal multiplicado por el factor al renglon que se encuentra procesando
            columna_eliminada=0
            for i in range(columna_eliminada, columna_eliminada < 4, columna_eliminada= columna_eliminada + 1):
                matriz[renglon_eliminado, columna_eliminada] = matriz[renglon_eliminado,columna_eliminada]-factor*matriz[renglon,columna_eliminada]

