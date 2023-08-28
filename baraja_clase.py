import random


class Baraja():
    def __init__(self):
        self.baraja = self.crearBaraja()
        self.cartas_jugadores = []

    def crearBaraja(self):
        # Crear baraja
        palos = ['o', 'c', 'e', 'b']
        cartas = ['A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']
        self.baraja = []
        for palo in palos:
            for carta in cartas:
                self.baraja.append(carta + palo)
        return self.baraja

    def mezclarBaraja(self):
        # Mezclar baraja
        for _ in range(200):
            posicion1 = random.randint(0, len(self.baraja) - 1)
            posicion2 = random.randint(0, len(self.baraja) - 1)
            self.baraja[posicion1], self.baraja[posicion2] = self.baraja[posicion2], self.baraja[posicion1]
        return self.baraja

    def repartir(self, mano, jugadores):
        # Validación datos de entrada
        if not isinstance(mano, int):
            raise TypeError('Mano debe ser un número entero')
        if not isinstance(jugadores, int):
            raise TypeError('Jugadores debe de ser un número entero')

        # Creación de listas jugadores
        listas_jugadores = []
        for _ in range(jugadores):
            listas_jugadores.append([])

        # Validar si hay cartas para todos los jugadores
        longitud_baraja = len(self.baraja)
        if longitud_baraja < mano * jugadores:
            if longitud_baraja < jugadores:
                raise ValueError('No hay suficientes cartas para cada jugador')
            else:
                # Repartir tantas cartas como se puedan
                for jugador in range(jugadores):
                    for _ in range(longitud_baraja//jugadores):
                        listas_jugadores[jugador - 1].append(self.baraja[0])
                        self.baraja.remove(self.baraja[0])
                self.cartas_jugadores = listas_jugadores
                print(
                    f'No se han podido repartir {mano} cartas para cada jugador ya que la baraja solo tiene {longitud_baraja} cartas, se han repartiro {longitud_baraja//jugadores}')
                return self.cartas_jugadores
        else:

            # Repartir cartas
            for _ in range(jugadores):
                jugadores = jugadores - 1
                for _ in range(mano):
                    listas_jugadores[jugadores].append(self.baraja[0])
                    self.baraja.remove(self.baraja[0])
            self.cartas_jugadores = listas_jugadores
            return self.cartas_jugadores
