from baraja_clase import Baraja

mano = Baraja(3, 3)
print(mano.baraja)
print()
mano.repartir(3, 3)
print(mano.baraja)
print()
mano.repartir(3, 3)
print(mano.baraja)
print()
mano.repartir(3, 3)
print(mano.baraja)
print()
mano.repartir(3, 3)
print(mano.cartas_jugadores)

'''
baraja = crearBaraja()
print(baraja)
print()
baraja = mezclarBaraja(baraja)
print(baraja)
print()
listas_jugadores = repartir(5, 5, baraja)
print(listas_jugadores)
print()
print(baraja)
'''
