import sys
import math


def error():
    print("BŁĄD: wystąpił problem z podanymi przez Ciebie argumentami. Użyj --help aby wyświetlić listę dostępnych opcji.")


def cez_kryptoanaliza_j(alphabet):
    while True:
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        try:
            file_extra = open("extra.txt", "r", encoding="utf-8")
            extra = str(file_extra.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku extra.txt")
            print("Plik extra.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_key = open("key-found.txt", "w", encoding="utf-8")
        file_decrypt = open("decrypt.txt", "w", encoding="utf-8")
        result = ""
        for i in range(0, 26):
            for letter in text:
                if letter.lower() in alphabet:
                    index = alphabet.index(letter.lower())
                    new = (index - i) % 26
                    if letter.isupper():
                        result += alphabet[new].upper()
                    else:
                        result += alphabet[new].lower()
                else:
                    result += letter
            if extra in result:
                key = i
                file_decrypt.write(result)
                file_key.write((str(key)))
                break
            else:
                result = ""
        if result == "":
            print("BŁĄD: nie udało się złamać szyfru.")
            break
        file_text.close()
        file_key.close()
        file_decrypt.close()
        file_extra.close()
        break


def cez_kryptoanaliza_k(alphabet):
    while True:
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_decrypt = open("decrypt.txt", "w", encoding="utf-8")
        for i in range(0, 26):
            result = ""
            for letter in text:
                if letter.lower() in alphabet:
                    index = alphabet.index(letter.lower())
                    new = (index - i) % 26
                    if letter.isupper():
                        result += alphabet[new].upper()
                    else:
                        result += alphabet[new].lower()
                else:
                    result += letter
            result += "\n"
            file_decrypt.write(result)
        file_text.close()
        file_decrypt.close()
        break


def a_kryptoanaliza_j(alphabet):
    key = []
    key2 = []
    results = []
    while True:
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        try:
            file_extra = open("extra.txt", "r", encoding="utf-8")
            extra = str(file_extra.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku extra.txt")
            print("Plik extra.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("decrypt.txt", "w", encoding="utf-8")
        file_kf = open("key-found.txt", "w", encoding="utf-8")
        result = ""
        for k in range(0, 26):
            if math.gcd(k, 26) == 1:
                for j in range(0, 26):
                    if (k * j) % 26 == 1:
                        for b in range(0, 26):
                            for letter in text:
                                if letter.lower() in alphabet:
                                    index = alphabet.index(letter.lower())
                                    new = j * (index - b) % 26
                                    if letter.isupper():
                                        result += alphabet[new].upper()
                                    else:
                                        result += alphabet[new].lower()
                                else:
                                    result += letter
                            if extra in result:
                                key.append(k)
                                key2.append(b)
                                results.append(result)
                                break
                            else:
                                result = ""

        if result == "":
            print("BŁĄD: nie udało się złamać szyfru.")
            break
        else:
            file_result.write(results[0])
            kf = str(key[0]) + " " + str(key2[0])
        file_kf.write(kf)
        file_text.close()
        file_result.close()
        file_kf.close()
        file_extra.close()
        break


def a_kryptoanaliza_k(alphabet):
    while True:
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("decrypt.txt", "w", encoding="utf-8")
        for k in range(0, 26):
            if math.gcd(k, 26) == 1:
                for j in range(0, 26):
                    if (k * j) % 26 == 1:
                        for b in range(0, 26):
                            result = ""
                            for letter in text:
                                if letter.lower() in alphabet:
                                    index = alphabet.index(letter.lower())
                                    new = j * (index - b) % 26
                                    if letter.isupper():
                                        result += alphabet[new].upper()
                                    else:
                                        result += alphabet[new].lower()
                                else:
                                    result += letter
                            result += "\n"
                            file_result.write(result)

        file_text.close()
        file_result.close()
        break


def afiniczny_en(alphabet):
    while True:
        try:
            file_key = open("key.txt", "r", encoding="utf-8")
            key = str(file_key.read())
            key = key.split(" ")
            a = int(key[0])
            b = int(key[1])
        except ValueError:
            print("Plik key.txt, który próbowano otworzyć, wywołał błąd. Są 3 możliwe rozwiązania: ")
            print("1. Upewnij się, że plik key.txt nie jest pusty.")
            print("2. Dla tej operacji potrzebne są 2 liczby. Upewnij się, że obie znajdują się w pliku key.txt i są oddzielone spacją.")
            print("3. Podane wartości nie są liczbami (np. są literą lub ciągiem znaków), lub liczby podano w niepoprawnym formacie.")
            print("Pamiętaj, że podawane przez Ciebie wartości a i b powinny być oddzielone spacją (np. 3 24).")
            break
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku key.txt")
            print("Plik key.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        if math.gcd(a, 26) != 1:
            print("BŁĄD: wartość a (pierwsza z podawanych liczb) musi spełniać warunek: NWD(a, 26) = 1")
            break
        try:
            file_text = open("plain.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku plain.txt")
            print("Plik plain.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("crypto.txt", "w", encoding="utf-8")
        result = ""
        for letter in text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new = (a * index + b) % 26
                if letter.isupper():
                    result += alphabet[new].upper()
                else:
                    result += alphabet[new].lower()
            else:
                result += letter
        file_result.write(result)
        file_text.close()
        file_result.close()
        file_key.close()
        break


def afiniczny_de(alphabet):
    while True:
        try:
            file_key = open("key.txt", "r", encoding="utf-8")
            key = str(file_key.read())
            key = key.split(" ")
            a = int(key[0])
            b = int(key[1])
            if math.gcd(a, 26) != 1:
                print("BŁĄD: wartość a (pierwsza z podawanych liczb) musi spełniać warunek: NWD(a, 26) = 1")
                break
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku key.txt")
            print("Plik key.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        except ValueError:
            print("Plik key.txt, który próbowano otworzyć, wywołał błąd. Są 3 możliwe rozwiązania: ")
            print("1. Upewnij się, że plik key.txt nie jest pusty.")
            print("2. Dla tej operacji potrzebne są 2 liczby. Upewnij się, że obie znajdują się w pliku key.txt i są oddzielone spacją.")
            print("3. Podane wartości nie są liczbami (np. są literą lub ciągiem znaków), lub liczby podano w niepoprawnym formacie.")
            print("Pamiętaj, że podawane przez Ciebie wartości a i b powinny być oddzielone spacją (np. 3 24).")
            break
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("decrypt.txt", "w", encoding="utf-8")
        result = ""
        for i in range(0, 28):
            if (i * a) % 26 == 1:
                a2 = i
        for letter in text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new = a2 * (index - b) % 26
                if letter.isupper():
                    result += alphabet[new].upper()
                else:
                    result += alphabet[new].lower()
            else:
                result += letter
        file_result.write(result)
        file_text.close()
        file_result.close()
        file_key.close()
        break


def cezara_en(alphabet):
    while True:
        try:
            file_key = open("key.txt", "r", encoding="utf-8")
            key = str(file_key.read())
            key = key.split(" ")
            key = int(key[0])
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku key.txt")
            print("Plik key.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        except ValueError:
            print("Plik key.txt, który próbowano otworzyć, wywołał błąd. Są 2 możliwe rozwiązania: ")
            print("1. Upewnij się, że plik key.txt nie jest pusty.")
            print("2. Podane wartości nie są liczbami (np. są literą lub ciągiem znaków).")
            break
        try:
            file_text = open("plain.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku plain.txt")
            print("Plik plain.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("crypto.txt", "w", encoding="utf-8")
        result = ""
        for letter in text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new = (index + key) % 26
                if letter.isupper():
                    result += alphabet[new].upper()
                else:
                    result += alphabet[new].lower()
            else:
                result += letter
        file_result.write(result)
        file_text.close()
        file_result.close()
        file_key.close()
        break



def cezara_de(alphabet):
    while True:
        try:
            file_key = open("key.txt", "r", encoding="utf-8")
            key = str(file_key.read())
            key = key.split(" ")
            key = int(key[0])
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku key.txt")
            print("Plik key.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        except ValueError:
            print("Plik key.txt, który próbowano otworzyć, wywołał błąd. Są 2 możliwe rozwiązania: ")
            print("1. Upewnij się, że plik key.txt nie jest pusty.")
            print("2. Podane wartości nie są liczbami (np. są literą lub ciągiem znaków).")
            break
        try:
            file_text = open("crypto.txt", "r", encoding="utf-8")
            text = str(file_text.read())
        except FileNotFoundError:
            print("BŁĄD: nie znaleziono pliku crypto.txt")
            print("Plik crypto.txt jest niezbędny do przeprowadzenia tej operacji.")
            break
        file_result = open("decrypt.txt", "w", encoding="utf-8")
        result = ""
        for letter in text:
            if letter.lower() in alphabet:
                index = alphabet.index(letter.lower())
                new = (index - key) % 26
                if letter.isupper():
                    result += alphabet[new].upper()
                else:
                    result += alphabet[new].lower()
            else:
                result += letter
        file_result.write(result)
        file_text.close()
        file_result.close()
        file_key.close()
        break


if __name__ == "__main__":
    a = str(sys.argv[1])
    try:
        b = str(sys.argv[2])
    except IndexError:
        b = ""
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    if a.lower() == "-c":
        if b.lower() == "-d":
            cezara_de(alphabet)
        elif b.lower() == "-e":
            cezara_en(alphabet)
        elif b.lower() == "-k":
            cez_kryptoanaliza_k(alphabet)
        elif b.lower() == "-j":
            cez_kryptoanaliza_j(alphabet)
        else:
            error()
    elif a.lower() == "-a":
        if b.lower() == "-d":
            afiniczny_de(alphabet)
        elif b.lower() == "-e":
            afiniczny_en(alphabet)
        elif b.lower() == "-k":
            a_kryptoanaliza_k(alphabet)
        elif b.lower() == "-j":
            a_kryptoanaliza_j(alphabet)
        else:
            error()
    elif a.lower() == "-d":
        if b.lower() == "-c":
            cezara_de(alphabet)
        elif b.lower() == "-a":
            afiniczny_de(alphabet)
        else:
            error()
    elif a.lower() == "-e":
        if b.lower() == "-c":
            cezara_en(alphabet)
        elif b.lower() == "-a":
            afiniczny_en(alphabet)
        else:
            error()
    elif a.lower() == "-k":
        if b.lower() == "-c":
            cez_kryptoanaliza_k(alphabet)
        elif b.lower() == "-a":
            a_kryptoanaliza_k(alphabet)
        else:
            error()
    elif a.lower() == "-j":
        if b.lower() == "-c":
            cez_kryptoanaliza_j(alphabet)
        elif b.lower() == "-a":
            a_kryptoanaliza_j(alphabet)
        else:
            error()
    elif a == "--help":
        print("/// Kryptografia zadanie 1 - program Cezar ///")
        print("\t-c: Szyfr Cezara")
        print("\t-a: Szyfr afiniczny")
        print("\t-d: dekodowanie")
        print("\t-e: kodowanie")
        print("\t-j: kryptoanaliza z tekstem jawnym")
        print("\t-k: kryptoanaliza w oparciu o kryptogram")
        print("/// Przykłady użycia: ///")
        print("\tpython cezar.py -c -d")
        print("\tpython cezar.py -a -j")
        print("\tpython cezar.py -e -a")
        print("\tpython cezar.py -k -c")
        print("/// Autor: Marta Rybarczyk ///")

    else:
        error()