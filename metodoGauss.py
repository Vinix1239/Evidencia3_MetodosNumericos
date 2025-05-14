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

#Imprimir la matriz
print("Tu matriz: ")
for fila in matriz:
    print(fila)

#Bucle for para la eliminación gaussiana
for renglon in range (3):
    pivote = matriz[renglon][renglon]

#Normalizar el renglon dividiendo cada elemento por el pivote
for columna in range(4):
    matriz[renglon][columna] /= pivote

#Eliminar elementos en la misma columna de otros renglones
for renglon_eliminado in range(3):
    if renglon_eliminado != renglon:
        factor = matriz[renglon_eliminado][renglon]
        for columna_eliminada in range(4):
            matriz[renglon_eliminado][columna_eliminada] -= factor*matriz[renglon][columna_eliminada]

