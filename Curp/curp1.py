#NOMBRE: Fernando Elias Garcia Trujillo
print("Este Programa Saca Los Primeros Dieciséis Caracteres de tu CURP")
nombre = input("Primer nombre: ").upper()

while nombre == "":
    print("ERROR, El nombre no puede quedar vacio")
    nombre = input("Primer nombre: ").upper()


Snombre = input("Segundo Nombre (Presiona Enter si no tienes): ").upper()

if Snombre == "":
    Snombre = "X"


ape1 = input("Primer Apellido: ").upper()

while ape1 == "":
    print("ERROR, El Primer Apellido no puede quedar vacio")
    ape1 = input("Primer Apellido: ").upper()


ape2 = input("Segundo Apellido (presiona Enter si no tienes): ").upper()

if ape2 == "":
    ape2 = "X"


año = int(input("Ingresa el año de nacimiento [1900,2026]: "))

while año < 1900 or año > 2026:
    print("Error, se espera un año entre 1900 y 2026.")
    año = int(input("Ingresa el año de nacimiento [1900,2026]: "))


mes = int(input("Ingresa El Mes De Nacimiento [1,12]: "))

while mes < 1 or mes > 12:
    print("Error, se espera un mes entre 1 y 12")
    mes = int(input("Ingresa El Mes De Nacimiento [1,12]: "))


dia = int(input("Ingresa El Dia De Nacimiento [1,31]: "))

while dia < 1 or dia > 31:
    print("Error, se espera un dia entre 1 y 31")
    dia = int(input("Ingresa El Dia De Nacimiento [1,31]: "))


año_str = str(año)
mes_str = str(mes).zfill(2)
dia_str = str(dia).zfill(2)


genero = input("Ingresa Tu Genero [Hombre o Mujer]: ").upper()

while genero == "" or (genero != "HOMBRE" and genero != "MUJER"):

    if genero == "":
        print("Error, El Genero No Puede Quedar Vacio")
    else:
        print("Error, Genero No Valido")

    genero = input("Ingresa Tu Genero [Hombre o Mujer]: ").upper()


print("En Que Estado Naciste\n") #el usuario elige el estado

print(f"{'1) Aguascalientes':<20}{'2) Baja California':<20}{'3) Baja California Sur'}")
print(f"{'4) Campeche':<20}{'5) Chiapas':<20}{'6) Chihuahua'}")
print(f"{'7) Ciudad de México':<20}{'8) Coahuila':<20}{'9) Colima'}")
print(f"{'10) Durango':<20}{'11) Guanajuato':<20}{'12) Guerrero'}")
print(f"{'13) Hidalgo':<20}{'14) Jalisco':<20}{'15) México'}")
print(f"{'16) Michoacán':<20}{'17) Morelos':<20}{'18) Nayarit'}")
print(f"{'19) Nuevo León':<20}{'20) Oaxaca':<20}{'21) Puebla'}")
print(f"{'22) Querétaro':<20}{'23) Quintana Roo':<20}{'24) San Luis Potosí'}")
print(f"{'25) Sinaloa':<20}{'26) Sonora':<20}{'27) Tabasco'}")
print(f"{'28) Tamaulipas':<20}{'29) Tlaxcala':<20}{'30) Veracruz'}")
print(f"{'31) Yucatán':<20}{'32) Zacatecas':<20}")

#Esta parte sirve para que el usuario elija un estado
estado = int(input("Selecciona Tu Estado: "))

match estado:
    case 1:
        estado = "AS"
    case 2:
        estado = "BC"
    case 3:
        estado = "BS"
    case 4:
        estado = "CC"
    case 5:
        estado = "CS"
    case 6:
        estado = "CH"
    case 7:
        estado = "DF"
    case 8:
        estado = "CL"
    case 9:
        estado = "CM"
    case 10:
        estado = "DG"
    case 11:
        estado = "GT"
    case 12:
        estado = "GR"
    case 13:
        estado = "HG"
    case 14:
        estado = "JC"
    case 15:
        estado = "MC"
    case 16:
        estado = "MN"
    case 17:
        estado = "MS"
    case 18:
        estado = "NT"
    case 19:
        estado = "NL"
    case 20:
        estado = "OC"
    case 21:
        estado = "PL"
    case 22:
        estado = "QT"
    case 23:
        estado = "QR"
    case 24:
        estado = "SP"
    case 25:
        estado = "SL"
    case 26:
        estado = "SR"
    case 27:
        estado = "TC"
    case 28:
        estado = "TS"
    case 29:
        estado = "TL"
    case 30:
        estado = "VZ"
    case 31:
        estado = "YN"
    case 32:
        estado = "ZS"
    case _:
        print("ERROR, El Estado Seleccionado No Es Valido")
        exit()




VOCALES = "AEIOU"


CONSONANTES = "BCDFGHJKLMNPQRSTVWXYZ"




if ape1[0] == "Ñ":
    letra1 = "X"
else:
    letra1 = ape1[0]




i = 1
vocal = ""

while i < len(ape1) and vocal == "":
    
    if ape1[i] in VOCALES:
        vocal = ape1[i]
    
    i += 1



if vocal == "":
    vocal = "X"




if ape2 == "X":
    letra3 = "X"

elif ape2[0] == "Ñ":
    letra3 = "X"

else:
    letra3 = ape2[0]




nombreCURP = nombre




if Snombre != "X":

    if nombre == "MARIA" or nombre == "MA" or nombre == "MA.":
        nombreCURP = Snombre

    elif nombre == "JOSE" or nombre == "J" or nombre == "J.":
        nombreCURP = Snombre


if nombreCURP[0] == "Ñ":
    letra4 = "X"
else:
    letra4 = nombreCURP[0]




PALABRAS_ALTISONANTES = ["LOCA"]




cuatro_letras = letra1 + vocal + letra3 + letra4




if cuatro_letras in PALABRAS_ALTISONANTES:
    vocal = "X"



i = 1
cons1 = ""

while i < len(ape1) and cons1 == "":
    
    if ape1[i] in CONSONANTES:
        cons1 = ape1[i]
    
    i += 1


if cons1 == "":
    cons1 = "X"




if ape2 == "X":

    cons2 = "X"

else:

    i = 1
    cons2 = ""

    while i < len(ape2) and cons2 == "":
        
        if ape2[i] in CONSONANTES:
            cons2 = ape2[i]
        
        i += 1

    if cons2 == "":
        cons2 = "X"




i = 1
cons3 = ""

while i < len(nombreCURP) and cons3 == "":
    
    if nombreCURP[i] in CONSONANTES:
        cons3 = nombreCURP[i]
    
    i += 1


if cons3 == "":
    cons3 = "X"




curp = (letra1 +vocal +letra3 +letra4 +año_str[2:] +mes_str +dia_str +genero[0] +estado +cons1 +cons2 +cons3)


print()
print("CURP:", curp)