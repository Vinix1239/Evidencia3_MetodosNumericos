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

#Bucle para poder iterar sobre cada renglón de la matriz
for i in range (renglon, renglon < 3, renglon= renglon+1):
    
    #Se selecciona el elemento que esta en diagonal como pivote
    pivote = matriz[renglon, renglon]

    #Toca normalizar el renglón dividiendo cada elemento por el pivote