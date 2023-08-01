def crearBaraja():
    palos = ['O', 'C', 'E', 'B']
    cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
    baraja = []

    for palo in palos:
        for carta in cartas:
            baraja.append(carta + palo)
    return baraja


baraja = (crearBaraja())


def barajar(baraja):
    baraja_barajada = set()
    for carta in baraja:
        baraja_barajada.add(carta)
    return baraja_barajada


baraja_barajada = (barajar(baraja))
print(baraja_barajada)
print(len(baraja_barajada))
