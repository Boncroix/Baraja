def crearBaraja():
    palos = ['O', 'C', 'E', 'B']
    cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    baraja = {}

    for palo in palos:
        for carta in cartas:
            baraja.add(carta + palo)
    return baraja
