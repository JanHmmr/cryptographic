"""
Eine Klasse für die Erstellung einer Txt-Datei
"""


def download(text, filename):
    """Lädt einen String als .txt-Datei herunter.

    Args:
        key (str): Der Textinhalt(key), der heruntergeladen werden soll.
        filename (str): Der gewünschte Dateiname.

    Returns:
        None"""
    texttup = {
        "Schlüssel : ": text,
    }

    with open(filename, "w", encoding="utf-8") as file:
        for text in texttup.items():
            file.write(str(text[0]) + str(text[1]) + "\n")
    print(f'Datei "{filename}" wurde heruntergeladen.')
