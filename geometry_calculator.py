# geometry_calculator.py

import math

def calculate_hypotenuse(side_a, side_b):
    """
    Berechnet die Hypotenuse eines rechtwinkligen Dreiecks.
    Verwendet den Satz des Pythagoras: c = sqrt(a^2 + b^2)
    """
    # TODO 1: Implementiere die Berechnung der Hypotenuse mit math.sqrt()
    # und dem Potenzoperator (**).
    return math.sqrt(side_a ** 2 + side_b ** 2)

def calculate_circle_area(radius):
    """
    Berechnet den Flächeninhalt eines Kreises.
    Formel: A = pi * r^2
    """
    # TODO 2: Implementiere die Berechnung des Flächeninhalts mit math.pi.
    return math.pi * radius ** 2

if __name__ == "__main__":
    print("Willkommen zum Geometrie-Rechner!")

    while True:
        print("\nWas möchten Sie berechnen?")
        print("1. Hypotenuse eines rechtwinkligen Dreiecks")
        print("2. Flächeninhalt eines Kreises")
        print("3. Beenden")

        choice = input("Ihre Wahl (1/2/3): ")

        if choice == '1':
            try:
                # TODO 3: Fordere den Benutzer auf, die Längen der Seiten a und b einzugeben.
                # Stelle sicher, dass die Eingaben in Zahlen umgewandelt werden (float()).
                side_a = float(input("Geben Sie die Länge der Seite a ein: "))
                side_b = float(input("Geben Sie die Länge der Seite b ein: "))

                # TODO 4: Rufe die Funktion calculate_hypotenuse auf und gib das Ergebnis aus.
                result = calculate_hypotenuse(side_a, side_b)
                print(f"Die Hypotenuse beträgt: {result}")

                #print("Bitte implementieren Sie die TODOs für die Hypotenuse-Berechnung!")

            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")
        elif choice == '2':
            try:
                # TODO 5: Fordere den Benutzer auf, den Radius einzugeben.
                radius = float(input("Geben Sie den Radius des Kreises ein: "))

                # TODO 6: Rufe die Funktion calculate_circle_area auf und gib das Ergebnis aus.
                result = calculate_circle_area(radius)
                print(f"Der Flächeninhalt des Kreises beträgt: {result}")

                #print("Bitte implementieren Sie die TODOs für die Kreisflächen-Berechnung!")

            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
        elif choice == '3':
            print("Auf Wiedersehen!")
            break
        else:
            print("Ungültige Wahl. Bitte wählen Sie 1, 2 oder 3.")
