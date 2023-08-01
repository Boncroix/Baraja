class Baraja():
    def __init__(self, mano, jugadores):
        self.palos = ['O', 'C', 'E', 'B']
        self.cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
        self.baraja = []
        self.baraja_mezclada = set()
        self.mano = mano
        self.jugadores = jugadores

        for self.palo in self.palos:
            for carta in self.cartas:
                self.baraja.append(carta + self.palo)

    def barajar(self):
        for carta in self.baraja:
            self.baraja_mezclada.add(carta)
        return list(self.baraja_mezclada)

    def repartir(self):
        cartas_jugadores = [[] for _ in range(self.jugadores)]
        for _ in range(self.jugadores):
            self.jugadores = self.jugadores - 1
            for _ in range(self.mano):
                cartas_jugadores[self.jugadores].append(self.baraja[0])
                self.baraja.remove(self.baraja[0])
        return cartas_jugadores

    def __str__(self):
        return self.cartas_jugadores

    def __repr__(self):
        return self.__str__()


baraja = Baraja()
