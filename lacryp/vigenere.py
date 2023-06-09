"""
    Eine Klasse, die das Vigenere-Verschlüsselungsverfahren implementiert.
"""


class Vigenere:
    """
    Die Vigenere-Klasse ermöglicht es, einen Text mit Hilfe der Vigenere-Verschlüsselungsmethode
    zu verschlüsseln oder zu entschlüsseln. Dabei wird der zu verarbeitende Text und der Schlüssel berücksichtigt.

    Attribute:
        text (str): Der zu verschlüsselnde oder zu entschlüsselnde Text.
        key (str): Der Schlüssel für die Verschlüsselung oder Entschlüsselung.

    Methoden:
        __init__(): Initialisiert eine Instanz der Vigenere-Klasse.
        encrypt(): Verschlüsselt den Text mit Hilfe der Vigenere-Verschlüsselungsmethode und dem angegebenen Schlüssel.
                   Gibt den verschlüsselten Text zurück.
        decrypt(): Entschlüsselt den Text mit Hilfe der Vigenere-Verschlüsselungsmethode und dem angegebenen Schlüssel.
                   Gibt den entschlüsselten Text zurück.
    """

    def __init__(self, *, text, key):
        self._text = text
        self._key = key

    def encrypt(self):
        """
        Verschlüsselt den Text mit Hilfe der Vigenere-Verschlüsselungsmethode und dem angegebenen Schlüssel.

        Returns:
            str: Der verschlüsselte Text.
        """
        encrypted_text = ""
        key_index = 0
        for char in self._text:
            if char.isalpha():
                key_char = self._key[key_index % len(self._key)]
                key_shift = ord(key_char.upper()) - ord("A")
                if char.isupper():
                    encrypted_char = chr(
                        (ord(char) - ord("A") + key_shift) % 26 + ord("A")
                    )
                else:
                    encrypted_char = chr(
                        (ord(char) - ord("a") + key_shift) % 26 + ord("a")
                    )
                encrypted_text += encrypted_char
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self):
        """
        Entschlüsselt den Text mit Hilfe der Vigenere-Verschlüsselungsmethode und dem angegebenen Schlüssel.

        Returns:
            str: Der entschlüsselte Text.
        """
        decrypted_text = ""
        key_index = 0
        for char in self._text:
            if char.isalpha():
                key_char = self._key[key_index % len(self._key)]
                key_shift = ord(key_char.upper()) - ord("A")
                if char.isupper():
                    decrypted_char = chr(
                        (ord(char) - ord("A") - key_shift) % 26 + ord("A")
                    )
                else:
                    decrypted_char = chr(
                        (ord(char) - ord("a") - key_shift) % 26 + ord("a")
                    )
                decrypted_text += decrypted_char
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
