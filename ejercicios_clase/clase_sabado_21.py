# Ejercicio 1

area_metropolitana = [
    ['Bucaramanga', 581000],
    ['Floridablanca', 267000],
    ['Giron', 260000],
    ['Piedecuesta', 163000]
]

total_poblacion = 0
for value in area_metropolitana:
    total_poblacion += value[1]

print("Ejercicio 1")
print("Total población AMB: " + str(total_poblacion))
print()


# Ejercicio 2
hijos_jose = 3
cantidad_mascotas = 2

total_mascotas_jose = hijos_jose * cantidad_mascotas
print("Ejercicio 2")
print("Mascotas en casa de Jose: " + str(total_mascotas_jose))
print()

# Ejercicio 3
estimacion_base10 = total_poblacion / 10
estimacion_mascotas_amb = estimacion_base10 * 3
print("Ejercicio 3")
print("Estimación mascotas AMB: " + str(estimacion_mascotas_amb))
print()

# Reto
tasa_crecimiento = 1.03
base = total_poblacion

print("Reto")
for a in range(1, 11):
    base *= 1.03
    print("Estimación año " + str(a) + ": " + str(base))