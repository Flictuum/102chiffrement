#!/usr/bin/python3

import os, sys
import numpy as np

#fonction de recuperation d'index
def index_of(base, c):
    i = 0
    while i < len(base):
        if base[i] == c:
            return i
        i += 1
    sys.exit("Phrase invalide, caractère autorisé: \"abcdefghijklmopqrstuvwxyz\" et \" \"")

#put_nbr_base
def putnbr_base(nbr, base):
    div = 1
    size_base = len(base)
    if int(nbr) < 0:
        print("-", end="")
        nbr *= -1
    while (div * size_base) <= nbr:
        div *= size_base
    while div >= 1:
        print(base[int(nbr/div)], end="")
        nbr = nbr % div
        div /= size_base
    return 0

#getnbr_base
def getnbr_base(s, base):
    res = 0
    sgn = 1
    i = 0
    if (s[i] == '-'):
        sgn *= -1
        i += 1
    while i < len(s):
        pos = 0
        while (pos < len(base)) and (base[pos] != s[i]):
            pos += 1
        if pos == len(base):
            sys.exit("Caractère non compris dans la base \"" + sys.argv[6] + "\".")
        res = res * len(base) + pos
        i += 1
    return (res * sgn)



''' debut de programme '''

#gestion nombre argument
if (len(sys.argv) != 8):
    sys.exit("Usage: ./102chiffrement {phrase} {key1} {key2} {key3} {key4} {base} " + 
             "{chiffrement: 0 ou dechiffrement: 1}")

#creation de la clef
det = int(sys.argv[2]) * int(sys.argv[5]) - int(sys.argv[3]) * int(sys.argv[4])
if (int(sys.argv[7]) == 0):
    key = np.matrix([[int(sys.argv[2]), int(sys.argv[4])],[int(sys.argv[3]), int(sys.argv[5])]])
    if (det == 0):
        print("Warning: Matrice non inversible, déchiffrement futur impossible.")
elif (int(sys.argv[7]) == 1):
    if (det == 0):
        sys.exit("Matrice non inversible, déchiffrement impossible")
    key = 1/det * np.matrix([[int(sys.argv[5]), int(sys.argv[4]) * -1],
                                  [int(sys.argv[3]) * -1, int(sys.argv[2])]])
else:
    sys.exit("Chiffrement = 0 ou dechiffrement = 1")

#chiffrement
if (int(sys.argv[7]) == 0):
    caract = [index_of(" abcdefghijklmnopqrstuvwxyz", c) for c in sys.argv[1]]
    x_max = int((len(caract) + 1) /2)
    crypt = [[0 for x in range(x_max)] for x in range(2)]
    x = 0
    i = 0
    while (x < x_max) and i < len(caract):
        y = 0
        while (y < 2) and i < len(caract):
            crypt[y][x] = caract[i]
            i += 1
            y += 1
        x += 1
    crypt = key * np.matrix(crypt)
    crypt = crypt.tolist()
    print("chiffrement de \"" + sys.argv[1] + "\" à l'aide la clé " + sys.argv[2] + " " + sys.argv[3] +
          " " + sys.argv[4] + " " + sys.argv[5] + " dans la base \"" + sys.argv[6] +"\"\n=>", end="")
    x = 0
    while x < x_max:
        y = 0
        while y < 2:
            print(" ", end="")
            putnbr_base(int(crypt[y][x]), sys.argv[6])
            y += 1
        x += 1
    print("")

#dechiffrement
elif (int(sys.argv[7]) == 1):
    caract = sys.argv[1]
    caract = caract.split()
    i = 0
    while i < len(caract):
        caract[i] = getnbr_base(caract[i], sys.argv[6])
        i += 1
    x_max = int(len(caract)/2)
    decrypt = [[0 for x in range(x_max)] for y in range(2)]
    x = 0
    i = 0
    while (x < x_max) and i < len(caract):
        y = 0
        while y < 2 and i < len(caract):
            decrypt[y][x] = caract[i]
            i += 1
            y += 1
        x += 1
    decrypt = key * np.matrix(decrypt)
    decrypt = decrypt.tolist()
    print("déchiffrement de \"" + sys.argv[1] + "\" à l'aide la clé " + sys.argv[2] + " " +
          sys.argv[3] + " " + sys.argv[4] + " " + sys.argv[5] + " dans la base \"" + sys.argv[6] +
          "\"\n=> ", end="")
    x = 0
    while x < x_max:
        y = 0
        while y < 2:
            if not (y == 1 and x == x_max - 1 and decrypt[y][x] == 0):
                 putnbr_base(int(decrypt[y][x]), " abcdefghijklmnopqrstuvwxyz")
            y += 1
        x += 1
    print("")
