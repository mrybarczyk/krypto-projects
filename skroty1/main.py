import bitarray
import numpy
import math


def fun(file1, file2, name):
    text1 = file1.read()[:-1]
    text2 = file2.read()[:-1]
    suma = 0
    l = 0
    for i in range(0, len(text1)):
        c1 = "{0:04b}".format(int(text1[i], 16))
        c2 = "{0:04b}".format(int(text2[i], 16))
        for b in range(0, len(c1)):
            l += 1
            if c1[b] != c2[b]:
                suma += 1
    p = '{0:.2f}%'.format((suma / l * 100))
    diff.write(name + " hash.txt: " + text1 + '\n')
    diff.write(name + " hash_.txt: " + text2 + '\n')
    diff.write("bit length: " + str(l) + "\n")
    diff.write("bit difference: " + str(suma) + ", percentage: " + p + "\n\n")
    file1.close()
    file2.close()


md5file1 = open("md5\\hash.txt", "r", encoding='utf-8')
md5file2 = open("md5\\hash_.txt", "r", encoding='utf-8')

sha1file1 = open("sha1\\hash.txt", "r", encoding='utf-8')
sha1file2 = open("sha1\\hash_.txt", "r", encoding='utf-8')

sha224file1 = open("sha224\\hash.txt", "r", encoding='utf-8')
sha224file2 = open("sha224\\hash_.txt", "r", encoding='utf-8')

sha256file1 = open("sha256\\hash.txt", "r", encoding='utf-8')
sha256file2 = open("sha256\\hash_.txt", "r", encoding='utf-8')

sha384file1 = open("sha384\\hash.txt", "r", encoding='utf-8')
sha384file2 = open("sha384\\hash_.txt", "r", encoding='utf-8')

sha512file1 = open("sha512\\hash.txt", "r", encoding='utf-8')
sha512file2 = open("sha512\\hash_.txt", "r", encoding='utf-8')

diff = open("diff.txt", "a", encoding='utf-8')

fun(md5file1, md5file2, "md5")
fun(sha1file1, sha1file2, "sha1")
fun(sha224file1, sha224file2, "sha224")
fun(sha256file1, sha256file2, "sha256")
fun(sha384file1, sha384file2, "sha384")
fun(sha512file1, sha512file2, "sha512")

diff.close()
