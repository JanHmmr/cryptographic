"""
    Eine Klasse, die das Caesar-Verschlüsselungsverfahren implementiert.
"""
from lacryp import utils


class Caesar:
    """
    Das Caesar-Verschlüsselungsverfahren verschlüsselt einen Text, indem jeder Buchstabe um eine bestimmte Anzahl
    von Positionen im Alphabet verschoben wird. Die Anzahl der Positionen wird durch den Schlüssel bestimmt.

    -param text: Der zu verschlüsselnde oder zu entschlüsselnde Text.
    -param key: Der Schlüssel für die Verschlüsselung oder Entschlüsselung.
    """

    def __init__(self, *, text, key):
        self._text = text
        self._key = int(key)

    def encrypt_letter(self, letter):
        """
        Verschlüsselt einen Buchstaben gemäß dem Caesar-Verschlüsselungsverfahren.

        -param letter: Der zu verschlüsselnde Buchstabe.
        -return: Der verschlüsselte Buchstabe.

        Das Verfahren verschlüsselt den Buchstaben basierend auf dem internen Schlüssel (self._key).
        Für kleinbuchstabige Buchstaben wird die Unicode-Nummer des Buchstabens um den Schlüssel erhöht.
        Wenn der resultierende Wert größer als 122 ist (Unicode-Nummer von 'z'), wird er auf den Bereich
        von 97 bis 122 reduziert (kleinbuchstabige Buchstaben im Alphabet).
        Für großbuchstabige Buchstaben wird der gleiche Ablauf durchgeführt, jedoch mit dem Bereich
        von 65 bis 90 (großbuchstabige Buchstaben im Alphabet).
        Der verschlüsselte Buchstabe wird zurückgegeben.
        """
        if letter in utils.exceptions_list:
            return ord(letter)
        if letter.islower():
            letter_key = (ord(letter) + self._key - 97) % 26 + 97
        else:
            letter_key = (ord(letter) + self._key - 65) % 26 + 65
        return letter_key

    def decrypt_letter(self, number):
        """
        Entschlüsselt eine Zahl und gibt den entsprechenden Buchstaben zurück.

        -param number: Die zu entschlüsselnde Zahl.
        -return: Der entschlüsselte Buchstabe.

        Das Verfahren entschlüsselt die Zahl basierend auf dem internen Schlüssel (self._key).
        Für Zahlen im Bereich von 97 bis 122 (kleinbuchstabige Buchstaben im Alphabet) wird die Zahl um den
        Schlüssel reduziert. Wenn der resultierende Wert kleiner als 97 ist, wird er auf den Bereich von
        97 bis 122 reduziert.
        Für Zahlen im Bereich von 65 bis 90 (großbuchstabige Buchstaben im Alphabet) wird der gleiche Ablauf
        durchgeführt, jedoch mit dem Bereich von 65 bis 90.
        Der entschlüsselte Buchstabe wird zurückgegeben.
        """
        if number in utils.exceptions_list:
            return chr(number)
        if 97 <= number <= 122:
            number_key = (number - self._key - 97) % 26 + 97
        else:
            number_key = (number - self._key - 65) % 26 + 65
        return chr(number_key)

    def encrypt(self):
        """
        Encrypts the text stored in the object using the encrypt_letter method.

        Returns:
        str: The encrypted text.
        """
        encrypted_text = [chr(self.encrypt_letter(char)) for char in self._text]
        return "".join(encrypted_text)

    def decrypt(self):
        """
        Decrypts the text stored in the object using the decrypt_letter method.

        Returns:
        str: The decrypted text.
        """

        decrypted_text = [self.decrypt_letter(ord(char)) for char in self._text]
        return "".join(decrypted_text)
