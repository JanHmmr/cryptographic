"""
    Eine Klasse zur Durchführung von Verschlüsselungs- und Entschlüsselungsoperationen
    unter Verwendung der Caesar- oder Vigenere-Verschlüsselungsmethode.
"""
from lacryp import caesar, vigenere, validate, export as test


class Cryption:
    """Eine Klasse zur Verarbeitung der Eingabe des Benutzers."""

    def __init__(self):
        """
        Initialisiert eine Instanz der Cryption-Klasse.
        """
        output = validate.UserInput()

        self.text = output[0]
        self.method = output[1]
        self.crypt = output[2]
        self.key = output[3]

    def cryption(self):
        """
        Ruft die Benutzereingabe-Funktion auf und führt je nach ausgewählter Verschlüsselungsmethode
        die entsprechende Verschlüsselungs- oder Entschlüsselungsoperation aus. Gibt das Ergebnis zurück.

        Rückgabewert:
            - output (str): Das Ergebnis der Verschlüsselungs- oder Entschlüsselungsoperation als Text.
        """

        if self.method == "c":
            caeser_obj = caesar.Caesar(text=self.text, key=self.key)
            if self.crypt == "e":
                decrypted_txt = caeser_obj.decrypt()
                print(
                    "Aus Sicherheitsgründen wird der verschlüsselte Text in einer Datei ausgelesen !"
                )
                test.download(decrypted_txt, "DeCrypted_Text")
                return decrypted_txt

            if self.crypt == "v":
                encrypted_txt = caeser_obj.encrypt()
                print(
                    "Aus Sicherheitsgründen wird der verschlüsselte Text in einer Datei ausgelesen !"
                )
                test.download(encrypted_txt, "Crypted_Text")
                return encrypted_txt

        elif self.method == "v":
            vigenere_obj = vigenere.Vigenere(text=self.text, key=self.key)
            if self.crypt == "e":
                decrypted_txt = vigenere_obj.decrypt()
                print(
                    "Aus Sicherheitsgründen wird der verschlüsselte Text in einer Datei ausgelesen !"
                )
                test.download(decrypted_txt, "DeCrypted_Text")
                return decrypted_txt

            if self.crypt == "v":
                encrypted_txt = vigenere_obj.encrypt()
                print(
                    "Aus Sicherheitsgründen wird der verschlüsselte Text in einer Datei ausgelesen !"
                )
                test.download(encrypted_txt, "Crypted_Text")
                return encrypted_txt
