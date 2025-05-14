#Metodo de Gauss
#Pedirle al usuario numeros para crear una matriz
matriz = []
print("Hola :>")
print("Ingresa 9 numeros para llenar una matriz por favor: ")
for i in range(3):
    fila = []
    for j in range(3):
        fila.append(float(input("Numero: ")))
        break
    matriz.append(fila)
for fila in matriz:
    print(fila)