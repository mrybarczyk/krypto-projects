import sys
import random
import fractions


def error():
    print("Podany parametr nie jest obslugiwany.")


def keygen():
    while True:
        try:
            elgamal = open("elgamal.txt", "r")
        except IOError:
            print("Nie znaleziono pliku elgamal.txt")
            break
        p = int(elgamal.readline())
        g = int(elgamal.readline())
        # b = int(random.uniform(1, 100))
        b = int(random.uniform(10000, 1000000))
        beta = pow(g, b, p)
        private = open("private.txt", "w")
        private.write(str(p))
        private.write("\n")
        private.write(str(g))
        private.write("\n")
        private.write(str(b))
        public = open("public.txt", "w")
        public.write(str(p))
        public.write("\n")
        public.write(str(g))
        public.write("\n")
        public.write(str(beta))
        private.close()
        public.close()
        elgamal.close()
        break


def enc():
    while True:
        try:
            plain = open("plain.txt", "r")
        except IOError:
            print("Nie znaleziono pliku plain.txt")
            break
        try:
            public = open("public.txt", "r")
        except IOError:
            print("Nie znaleziono pliku public.txt")
            break
        p = int(public.readline())
        g = int(public.readline())
        beta = int(public.readline())
        m = int(plain.read())
        # k = int(random.uniform(1, 100))
        k = int(random.uniform(10000, 1000000))
        if m >= p:
            print("Blad: niespelniony warunek m < p")
            break
        s1 = pow(g, k, p)
        s2 = (m * pow(beta, k, p)) % p
        crypto = open("crypto.txt", "w")
        crypto.write(str(s1))
        crypto.write("\n")
        crypto.write(str(s2))
        crypto.close()
        break


def dec():
    while True:
        try:
            crypto = open("crypto.txt", "r")
        except IOError:
            print("Nie znaleziono pliku crypto.txt")
            break
        try:
            private = open("private.txt", "r")
        except IOError:
            print("Nie znaleziono pliku private.txt")
            break
        p = int(private.readline())
        g = int(private.readline())
        b = int(private.readline())
        gk = int(crypto.readline())
        mbetak = int(crypto.readline())
        print("Zaczekaj do zakonczenia zadania.")
        x = 1
        while True:
            if pow(g, x, p) == gk:
                break
            x += 1
        mk = pow(g, b, p)
        key = pow(mk, x, p)
        y = pow(key, p-2, p)
        m = (mbetak * y) % p
        decrypt = open("decrypt.txt", "w")
        decrypt.write(str(m))
        decrypt.close()
        private.close()
        crypto.close()
        print("Gotowe!")
        break


def inv(k2, p2):
    i = 0
    j = 1
    mem = p2
    if p2 == 1:
        j = 0
    else:
        while k2 > 1:
            m = k2 / p2
            temp = p2
            p2 = k2 % p2
            k2 = temp
            temp = i
            i = j - m * i
            j = temp
        if j < 0:
            j += mem
    return j


def signature():
    while True:
        try:
            private = open("private.txt", "r")
        except IOError:
            print("Nie znaleziono pliku private.txt")
            break
        try:
            plain = open("plain.txt", "r")
        except IOError:
            print("Nie znaleziono pliku plain.txt")
            break
        m = int(plain.read())
        p = int(private.readline())
        g = int(private.readline())
        b = int(private.readline())
        while True:
            k = random.randrange(1, p)
            if fractions.gcd(k, p-1) == 1:
                break
        r = pow(g, k, p)
        x = int(((m - (b*r)) * inv(k, p-1)) % (p - 1))
        s = open("signature.txt", "w")
        s.write(str(r))
        s.write("\n")
        s.write(str(x))
        s.close()
        private.close()
        plain.close()
        break


def verifying():
    while True:
        try:
            s = open("signature.txt", "r")
        except IOError:
            print("Nie znaleziono pliku signature.txt")
            break
        try:
            public = open("public.txt", "r")
        except IOError:
            print("Nie znaleziono pliku public.txt")
            break
        try:
            plain = open("plain.txt", "r")
        except IOError:
            print("Nie znaleziono pliku plain.txt")
            break
        r = int(s.readline())
        x = int(s.readline())
        p = int(public.readline())
        g = int(public.readline())
        beta = int(public.readline())
        m = int(plain.read())
        no1 = pow(g, m, p)
        print(str(no1))
        no2 = (pow(beta, r, p) * pow(r, x, p)) % p
        print(str(no2))
        if p > r >= 1 and no1 == no2:
            test = "OK"
        else:
            test = "SIGNATURES DO NOT MATCH"
        print(test)
        v = open("verify.txt", "w")
        v.write(test)
        v.close()
        s.close()
        public.close()
        plain.close()
        break


if __name__ == "__main__":
    a = str(sys.argv[1])
    if a.lower() == "-k":
        keygen()
    elif a.lower() == "-e":
        enc()
    elif a.lower() == "-d":
        dec()
    elif a.lower() == "-s":
        signature()
    elif a.lower() == "-v":
        verifying()
    elif a.lower() == "--help":
        print("/// Kryptografia zadanie 5 - program ElGamal ///")
        print("\t-k: Generowanie kluczy")
        print("\t-e: Szyfrowanie")
        print("\t-d: Odszyfrowanie")
        print("\t-s: Generowanie podpisu")
        print("\t-v: Weryfikacja podpisu")
        print("/// Autor: Marta Rybarczyk ///")
    else:
        error()
