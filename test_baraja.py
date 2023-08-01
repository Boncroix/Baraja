from baraja import *

baraja = crearBaraja()
print(baraja)
print()
baraja = mezclar(baraja)
print(baraja)
print()
listas_jugadores = repartir(5, 5, baraja)
print(listas_jugadores)
print()
print(baraja)
