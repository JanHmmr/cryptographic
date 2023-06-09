from lacryp import Cryption
# Hier ist die Klasse für das Verschlüssen/Entschlüsseln mit der User-Interaktion
cr1 = Cryption().cryption()

from lacryp import Caesar
# Hier ist ein Test für Verschlüsseln mit Hilfe von Caesar-methode
c1 = Caesar(text="Hallo", key=123)
print(c1.encrypt())  # --> Ateeh


from lacryp import Vigenere

# Hier ist ein Test für Verschlüsseln mit Hilfe von Vigenere-methode
v1 = Vigenere(text="Hallo", key="abc")
print(v1.encrypt())


# Hier ist das Entschlüsseln von dem gleichen Wort, sodass Ergebnis Hallo ist
v2 = Vigenere(text=v1.encrypt(), key="abc")
print(v2.decrypt())
