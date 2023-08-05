import random


def crearBaraja():
    palos = ['O', 'C', 'E', 'B']
    cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    baraja = []

    for palo in palos:
        for carta in cartas:
            baraja.append(carta + palo)
    return baraja


def mezclarBaraja(baraja):
    for _ in range(200):
        posicion1 = random.randint(0, len(baraja) - 1)
        posicion2 = random.randint(0, len(baraja) - 1)
        baraja[posicion1], baraja[posicion2] = baraja[posicion2], baraja[posicion1]
    return baraja


def repartir(mano, jugadores, baraja):
    listas_jugadores = [[] for _ in range(jugadores)]
    for _ in range(jugadores):
        jugadores = jugadores - 1
        for _ in range(mano):
            listas_jugadores[jugadores].append(baraja[0])
            baraja.remove(baraja[0])
    return listas_jugadores
