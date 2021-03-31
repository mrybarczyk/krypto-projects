from PIL import Image
import numpy
import hashlib
import bitarray


# definicje funkcji #################################################

def gen():
    blocks = []
    for i in range(0, plain_height, block_height):
        for j in range(0, plain_width, block_width):
            if j + block_width < plain_width:
                y2 = j + block_width
            else:
                y2 = plain_width
            if i + block_height < plain_height:
                x2 = i + block_height
            else:
                x2 = plain_height
            blocks.append([i, j, x2, y2])
    return blocks


def ecb(pixels):
    for block in blocks:
        pixels = encrypting(pixels, block[0], block[1], block[2], block[3])
    return pixels


def cbc(pixels):
    pre = str(numpy.random.randint(0, 2, block_height * block_width))
    pixels = xor(pixels, pre, blocks[0][0], blocks[0][1], blocks[0][2], blocks[0][3])
    encrypting(pixels, blocks[0][0], blocks[0][1], blocks[0][2], blocks[0][3])
    for block in blocks:
        pixels = xor(pixels, pre, block[0], block[1], block[2], block[3])
        pixels = encrypting(pixels, block[0], block[1], block[2], block[3])
        pre = get_key(pixels, block[0], block[1], block[2], block[3])
    return pixels


def encrypting(pixels, x1, y1, x2, y2):
    key = get_key(pixels, x1, y1, x2, y2)
    index = 0
    h = hashlib.md5()
    h.update(key)
    array = bitarray.bitarray()
    array.frombytes(h.hexdigest().encode('utf-8'))
    for i in range(x1, x2):
        for j in range(y1, y2):
            if array[index]:
                pixels[i][j] = [0, 0, 0]
            else:
                pixels[i][j] = [255, 255, 255]
            index += 1
    return pixels


def get_key(pixels, x1, y1, x2, y2):
    key = numpy.zeros(block_height * block_width)
    index = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if pixels[i][j][0] == pixels[i][j][1] == pixels[i][j][2] == 0:
                key[index] = 1
            else:
                key[index] = 0
            index += 1
    return key


def xor(pixels, pre, x1, y1, x2, y2):
    index = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if pre[index]:
                if pixels[i][j][0] == pixels[i][j][1] == pixels[i][j][2] == 0:
                    pixels[i][j] = [255, 255, 255]
                else:
                    pixels[i][j] = [0, 0, 0]
            else:
                if pixels[i][j][0] == pixels[i][j][1] == pixels[i][j][2] == 255:
                    pixels[i][j] = [255, 255, 255]
                else:
                    pixels[i][j] = [0, 0, 0]
            index += 1
    return pixels


# main ##############################################################
# Otwierany obrazek musi być kwadratową 24-bitową bitmapą

block_height = 4
block_width = 4

while True:
    try:
        plain = Image.open("plain.bmp")
    except FileNotFoundError:
        print("Nie znaleziono pliku graficznego. Potrzebna jest kwadratowa 24-bitowa bitmapa o nazwie \"plain.bmp\"")
        break

    plain_height, plain_width = plain.size

    if plain_height != plain_width:
        print("Upewnij się, że twoja 24-bitowa bitmapa jest kwadratowa.")
        break

    blocks = gen()

    ecb_array = ecb(numpy.array(plain))
    cbc_array = cbc(numpy.array(plain))

    result_ecb = Image.fromarray(ecb_array).save("ecb_crypto.bmp")
    result_cbc = Image.fromarray(cbc_array).save("cbc_crypto.bmp")
    break
