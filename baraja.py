def crearBaraja():
    palos = ['O', 'C', 'E', 'B']
    cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    baraja = []

    for palo in palos:
        for carta in cartas:
            baraja.append(carta + palo)
    return baraja


def mezclar(baraja):
    baraja_mezclada = set()
    for carta in baraja:
        baraja_mezclada.add(carta)
    return list(baraja_mezclada)


def repartir(mano, jugadores, baraja):
    listas_jugadores = [[] for _ in range(jugadores)]
    for _ in range(jugadores):
        jugadores = jugadores - 1
        for _ in range(mano):
            listas_jugadores[jugadores].append(baraja[0])
            baraja.remove(baraja[0])
    return listas_jugadores
