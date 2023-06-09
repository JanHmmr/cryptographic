"""Eine klasse für die Eingaben von dem Benutzer"""
from lacryp import export as test


def UserInput():
    """
    Fordert den Benutzer auf, Text einzugeben, eine Verschlüsselungsmethode (Vigenere oder Caesar) auszuwählen
    und andere erforderliche Informationen einzugeben. Gibt die eingegebenen Informationen zurück.

    Rückgabewerte:
        - text (str): Der eingegebene Text.
        - method (str): Die ausgewählte Verschlüsselungsmethode ("v" für Vigenere oder "c" für Caesar).
        - crypt (str): Die Auswahl, ob der Text verschlüsselt ("v") oder entschlüsselt ("e") werden soll.
        - key (str oder int): Der eingegebene Schlüssel für die Verschlüsselungsmethode.
          Bei der Caesar-Verschlüsselung muss es eine Zahl zwischen 1 und 26 sein, bei der Vigenere-Verschlüsselung
          muss es ein Buchstaben-String sein.
    """

    text = input("Gebe hier deinen Text ein!")

    while True:
        method = input(
            "Wähle deine Verschlüsselungsmethode: Vigenere(v) oder Caesar(c)"
        )

        if method in ["c", "C", "caesar", "Caesar"]:

            while True:

                crypt = input("Soll entschlüsselt(e) oder verschlüsselt(v) werden?")

                if crypt in [
                    "e",
                    "v",
                    "entschlüsseln",
                    "verschlüsseln",
                    "Entschlüsseln",
                    "Verschlüsseln",
                ]:

                    while True:
                        try:
                            key = int(input("Welchen Key? Merke dir diesen gut: "))
                        except TypeError:
                            print("Bitte gib NUR Zahlen ein!")
                            continue

                        test.download(key, "Schlüssel")

                        return text, method, crypt, key

                print("Bitte e oder v eingeben !!!!")

        elif method in ["v", "V", "vigenere", "Vigenere"]:

            while True:

                crypt = input("Soll entschlüsselt(e) oder verschlüsselt(v) werden?")

                if crypt in [
                    "e",
                    "v",
                    "entschlüsseln",
                    "verschlüsseln",
                    "Entschlüsseln",
                    "Verschlüsseln",
                ]:

                    while True:

                        key = input("Welchen Key? Merke dir diesen gut: ")

                        if key.isalpha():
                            test.download(key, "Schlüssel")
                            return text, method, crypt, key

                        print("Bitte gib NUR Buchstaben ein!")

                else:
                    print("Error")
                    continue

        print("Bitte wähle v oder c")
