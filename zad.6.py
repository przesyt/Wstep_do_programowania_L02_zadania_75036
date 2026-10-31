litera = input("Wprowadź literę: ")
# Sprawdzenie, czy znak jest literą
if litera.isalpha() and len(litera) == 1:
    # Sprawdzenie, czy litera jest duża
    if litera.isupper():
        print(f"Litera {litera} jest dużą literą")
        # Sptawdzenie, czy litera jest mała
    elif litera.islower():
        print(f"Litera {litera} jest małą literą")
else:
    print("Podany znak nie jest literą")
