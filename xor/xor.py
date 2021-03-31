import sys
# https://inf.ug.edu.pl/~amb/krypto-lab/xor.html


def test_male(letter):
    if 32 == ord(letter) or 97 <= ord(letter) <= 122:
        return True
    return False


def test_duze(letter):
    if 65 <= ord(letter) <= 90:
        return True
    return False


def przyklad():
    while True:
        try:
            orig = open("orig.txt", "r", encoding='utf-8')
        except FileNotFoundError:
            print("Brak pliku orig.txt")
            break
        plain = open("plain.txt", "w+", encoding='utf-8')
        text = orig.read()
        text = text.replace('\n', ' ')
        text = text.replace('\t', ' ')
        new_text = []
        for letter in text:
            if test_male(letter):
                new_text.append(letter)
            if test_duze(letter):
                new_text.append(letter.lower())
        newtext = [new_text[i:i + 64] for i in range(0, len(new_text), 64)]
        for line in newtext:
            for letter in line:
                plain.write(letter)
            plain.write("\n")
        orig.close()
        plain.close()
        break


def szyfrowanie():
    while True:
        try:
            plain = open("plain.txt", "r", encoding='utf-8')
        except FileNotFoundError:
            print("Brak pliku plain.txt")
            print("Spróbuj najpierw uruchomić xor.py z opcją -p")
            break
        try:
            keyfile = open("key.txt", "r", encoding='utf-8')
        except FileNotFoundError:
            print("Brak pliku klucza key.txt")
            break
        crypted = open("crypto.txt", "w", encoding='utf-8')
        crypted_not_ascii = open("crypto-text.txt", "w", encoding='utf-8')
        key2 = keyfile.read()
        key = list(key2)
        c = ''
        try:
            for letter in key:
                if test_duze(letter):
                    letter.lower()
                if not (test_duze(letter) or test_male(letter)):
                    raise KeyError
        except KeyError:
            print("Podany przez Ciebie klucz zawiera niedozwolone znaki.")
            print("Pamiętaj, że klucz może składać się tylko z liter a-z i musi mieć 64 znaki długości.")
            break
        text = plain.readlines()
        try:
            for line in text:
                if len(line) == 65:
                    for i, letter in enumerate(line):
                        if i != 64:
                            c = ord(letter) ^ ord(key[i])
                            crypted.write(str(c))
                            crypted.write(",")
                        crypted_not_ascii.write(chr(c))
                    crypted.write('\n')
        except IndexError:
            print("Wpisany przez Ciebie klucz jest za krótki.")
            print("Pamiętaj, że klucz może składać się tylko z liter a-z i musi mieć 64 znaki długości.")
            break
        keyfile.close()
        plain.close()
        crypted.close()
        crypted_not_ascii.close()
        break

def kryptoanaliza():
    while True:
        try:
            crypted = open("crypto.txt", "r", encoding='utf-8')
        except FileNotFoundError:
            print("Brak pliku crypto.txt")
            print("Uruchom najpierw xor.py z opcją -p, a potem -e")
            break
        decrypted = open("decrypt.txt", "w", encoding='utf-8')
        found = open("found-key.txt", "w", encoding='utf-8')
        key = []
        text = crypted.read()
        text = text.replace('\n', '')
        text = text.split(',')
        text.remove(text[len(text)-1])
        newtext = [text[i:i + 64] for i in range(0, len(text), 64)]
        for i in range(0, 64):
            c = 32
            for j in range(0, len(newtext)-2):
                a = int(newtext[j][i]) ^ int(newtext[j + 1][i])
                # ord(' ') ^ ord('a') = 65
                # ord(' ') ^ ord('z') = 90
                if 65 <= a <= 90:
                    a = int(newtext[j + 1][i]) ^ int(newtext[j + 2][i])
                    if not 65 <= a <= 90:
                        c = int(newtext[j][i]) ^ 32
            key.append(c)
            found.write(chr(c))
        for line in newtext:
            for i, c in enumerate(line):
                decrypted.write(chr(int(c) ^ int(key[i])))
            decrypted.write('\n')
        crypted.close()
        decrypted.close()
        found.close()
        break


def error():
    print("BŁĄD: wystąpił problem z podanymi przez Ciebie argumentami. Użyj --help aby wyświetlić listę dostępnych opcji.")


if __name__ == "__main__":
    while True:
        try:
            a = str(sys.argv[1])
        except IndexError:
            error()
            break
        if a.lower() == "-p":
            przyklad()
        elif a.lower() == "-e":
            szyfrowanie()
        elif a.lower() == "-k":
            kryptoanaliza()
        elif a == "--help":
            print("/// Kryptografia zadanie 2 - program Xor ///")
            print("\t-p: przygotowanie tekstu do przykładu działania")
            print("\t-e: szyfrowanie")
            print("\t-k: kryptoanaliza")
            print("/// Autor: Marta Rybarczyk ///")
        else:
            error()
        break
