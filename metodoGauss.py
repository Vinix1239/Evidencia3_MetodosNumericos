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
for fila in matriz:
    print(fila)