def cifrar(mensaje, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for letra in mensaje:
        if letra in abecedario:
            for i in range(len(abecedario)):
                if letra == abecedario[i]:
                    posicion = i + desplazamiento

                    resultado += abecedario[posicion]
                    break
        else:
            resultado += letra

    return resultado

def descifrar(mensaje, desplazamiento):
    abecedario = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    resultado = ""

    for letra in mensaje:
        if letra in abecedario:
            for i in range(len(abecedario)):
                if letra == abecedario[i]:
                    posicion = i - desplazamiento

                    resultado += abecedario[posicion]
                    break
        else:
            resultado += letra

    return resultado

print("ESTE PROGRAMA CIFRA O DECIFRA UN MENSAJE")
while True:
    try:
        selec = int(input("Que Quieres Hacer? Cifrar o Descifrar [1,2] = "))
        if selec >= 1 and selec <= 2:
            break
        else:
            print("ERROR: Ingresa un numero entre [1,2] = ")
    except ValueError:
        print("ERROR: Tiene que ser un Numero Entero")

mensaje = input("\nIngresa el Mensaje: ")
desplazamiento = int(input("Desplazamiento: "))

if selec == 1:
    mensaje_cifrado = cifrar(mensaje, desplazamiento)
    print("Mensaje :", mensaje_cifrado)
else:
    mensaje_descifrado = descifrar(mensaje, desplazamiento)
    print("Mensaje :", mensaje_descifrado)


