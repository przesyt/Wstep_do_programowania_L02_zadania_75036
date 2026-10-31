with open("notowania_gieldowe.txt", "r") as plik:
    for line in plik:
# end= "", Python dodaje nowej linii
        print(line, end="")
