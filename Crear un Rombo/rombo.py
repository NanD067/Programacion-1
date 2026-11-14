
n = int(input("Ingrese el valor de n (1-20): "))

if n < 1 or n > 20:
    print("ERROR: el valor de n debe estar entre 1 y 20.")
else:
    caracter = input("Ingrese el carácter que desea utilizar: ") #El usuario elige que caracter quiere usar

    
    for i in range(1, n + 1):
        espacios = n - i
        caracteres = 2 * i - 1

        print(" " * espacios + caracter * caracteres)

    
    for i in range(n - 1, 0, -1):
        espacios = n - i
        caracteres = 2 * i - 1

        print(" " * espacios + caracter * caracteres)