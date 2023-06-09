"""
Erstellt eine Liste von Ausnahmen für Zeichen außerhalb des Bereichs druckbarer ASCII-Zeichen.

Ausnahmen werden für Zeichen identifiziert, die weder alphabetisch (Buchstaben) noch numerisch (Ziffern) sind.

Rückgabe:
    exceptions_list (Liste): Eine Liste, die die numerischen und entsprechenden Zeichenrepräsentationen der Ausnahmen enthält.

"""

exceptions_list = []
for index in range(32, 126):
    if chr(index).isalpha() or chr(index).isdigit():
        continue
    exceptions_list.append(index)
    exceptions_list.append(chr(index))
