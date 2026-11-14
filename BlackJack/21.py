import random


def crear_mazo():
    palos = ["♠", "♥", "♦", "♣"]
    rangos = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    mazo = [(r, p) for r in rangos for p in palos]
    random.shuffle(mazo)
    return mazo


def valor(mano):
    total = 0
    ases = 0
    for rango, _ in mano:
        if rango == "A":
            total += 11
            ases += 1
        elif rango in ("J", "Q", "K"):
            total += 10
        else:
            total += int(rango)
    while total > 21 and ases:
        total -= 10
        ases -= 1
    return total


def crear_carta(rango, palo, oculta=False):
    """Crea una carta como matriz de 3 filas x 5 columnas."""
    carta = [
        ["+", "-", "-", "-", "+"],
        ["|", " ", " ", " ", "|"],
        ["+", "-", "-", "-", "+"],
    ]

    if oculta:
        for c in range(1, 4):
            carta[1][c] = "#"
    else:
        # Rango y palo juntos, por ejemplo "10♠" o "A♥"
        for i, caracter in enumerate(rango + palo):
            carta[1][1 + i] = caracter

    return carta


def mostrar(mano, ocultar=False):
    cartas = []
    for i, (rango, palo) in enumerate(mano):
        cartas.append(crear_carta(rango, palo, oculta=(ocultar and i == 1)))

    # Se imprime fila por fila, juntando las cartas una al lado de otra
    for fila in range(3):
        print(" ".join("".join(carta[fila]) for carta in cartas))


def pedir_apuesta(dinero):
    while True:
        texto = input(f"\nTienes ${dinero}. ¿Cuánto apuestas? ")
        if texto.isdigit() and 1 <= int(texto) <= dinero:
            return int(texto)
        print("Apuesta inválida.")


def jugar(dinero):
    """Juega una ronda y devuelve el dinero que te queda."""
    apuesta = pedir_apuesta(dinero)
    mazo = crear_mazo()
    jugador = [mazo.pop(), mazo.pop()]
    crupier = [mazo.pop(), mazo.pop()]

    # Turno del jugador
    while True:
        print(f"\nApuesta: ${apuesta}")
        print("\nCrupier:")
        mostrar(crupier, ocultar=True)
        print(f"\nTus cartas ({valor(jugador)}):")
        mostrar(jugador)

        if valor(jugador) > 21:
            print(f"\n¡Te pasaste! Pierdes ${apuesta}.")
            return dinero - apuesta
        if valor(jugador) == 21:
            break

        if input("\n¿Pedir carta (p) o plantarte (q)? ").lower() == "p":
            jugador.append(mazo.pop())
        else:
            break

    # Turno del crupier
    while valor(crupier) < 17:
        crupier.append(mazo.pop())

    print(f"\nCrupier ({valor(crupier)}):")
    mostrar(crupier)
    print(f"\nTus cartas ({valor(jugador)}):")
    mostrar(jugador)

    if valor(crupier) > 21 or valor(jugador) > valor(crupier):
        print(f"\n¡Ganaste ${apuesta}!")
        return dinero + apuesta
    elif valor(jugador) < valor(crupier):
        print(f"\nPerdiste ${apuesta}.")
        return dinero - apuesta
    else:
        print("\nEmpate. Recuperas tu apuesta.")
        return dinero


dinero = 100
while dinero > 0:
    dinero = jugar(dinero)
    if dinero == 0:
        print("\nTe quedaste sin dinero. ¡Fin del juego!")
        break
    if input("\n¿Jugar otra vez? (s/n) ").lower() != "s":
        break

print(f"\nTe vas con ${dinero}. ¡Gracias por jugar!")