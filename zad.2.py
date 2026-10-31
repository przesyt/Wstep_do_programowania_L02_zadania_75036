x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
z = float(input("Podaj z: "))
# Porzadkowanie liczb
if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y
# Wynik końcowy
print(f"Liczby w kolejności rosnącej: {x}, {y}, {z}")