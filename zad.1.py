wynik = int(input("Podaj liczbę punktów: "))
if wynik >= 80:
    print("Egzamin zaliczony w terminie 0.")
elif wynik >= 50:
    print("Możliwe poprawienie egzaminu.")
elif wynik < 50:
    print("Konieczne poprawienie egzaminu.")