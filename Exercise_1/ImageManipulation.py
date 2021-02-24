import cv2
import numpy as np
import Utilities
from scipy.spatial import KDTree
#from webcolors import (
#    css3_hex_to_names,
#    hex_to_rgb,
#)

# Example for basic pixel based image manipulation:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_core/py_basic_ops/py_basic_ops.html

# Task 1:
# Implement some kind of noticeable image manipulation in this function
# e.g. channel manipulation, filter you already know, drawings on the image etc.


def myFirstImageManipulation(img):
    # Rotiert das Bild
    imgEdited = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    # Splittet die Channel in b, g, r
    b, g, r = cv2.split(imgEdited)

    # Fügt sie wieder in anderer Reihenfolge zusammen
    imgEdited = cv2.merge([r, g, b])

    # Bild speichern
    saveImage(imgEdited)

    # Bild Informationen ausgeben
    printImageDetails(imgEdited)

    # Bild anzeigen
    showImage(imgEdited)


def showImage(img):
    cv2.imshow("Image loaded", img)
    cv2.waitKey(0)


def changeGrayscale(img):
    # Erstellt das Grayscale Bild
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Bild Informationen ausgeben
    printImageDetails(img)

    # Bild anzeigen
    showImage(img)


def saveImage(img):
    cv2.imwrite('./SavedImage.jpg', img)
    print('Image was saved.')

#####################################################################################
# Extra:    Print the basic image properties to the console:
#           width, height, number of channels, number of pixels, pixel type,
#           the color of the first pixel of the image,
#           Color of the first pixel in the second row
#           Color of the first pixel in the second column
#           This function should work for color and for grayscale images


def printImageDetails(img):
    # Width Zeile
    print('Höhe des Bildes: ', img.shape[0], ' Pixel.')

    # Height Spalte
    print('Breite des Bildes: ', img.shape[1], ' Pixel.')

    # Number of Channels
    if len(img.shape) > 2:
        print('Anzahl Channel: ', img.shape[2])
    else:
        print('Grayscale Bilder bekommen keinen Channel zugewiesen und besitzen nur einen.')

    # Number of Pixels
    print('Gesamtanzahl von Pixeln: ', img.size)

    # Pixel Type dtype
    px = img[0, 0]
    print('Type: ', px.dtype)

    # Farbe des ersten Pixel in HEX z.B. [255 255 255]
    if len(img.shape) > 2:
        px = img[0, 0]
        try:
            print('Erster Pixel', convert_rgb_to_names(px))
        except NameError:
            print("Colornames could not be written due to unexpexted error. \n Der Pixel hat folgende Farbwerte: ", px)
    else:
        print('Erster Pixel: ', img[0, 0])

    # Farbe des ersten Pixel in zweite Zeile in HEX z.B. [255 255 255]
    if len(img.shape) > 2:
        px = img[1, 0]
        try:
            print('Erster Pixel zweite Reihe', convert_rgb_to_names(px))
        except NameError:
            print("Colornames could not be written due to unexpexted error. \n Der Pixel hat folgende Farbwerte: ", px)
    else:
        print('Erster Pixel zweite Reihe: ', img[1, 0])

    # Farbe des ersten Pixel in zweite Spalte in HEX z.B. [255 255 255]
    if len(img.shape) > 2:
        px = img[0, 1]
        try:
            print('Erster Pixel zweite Spalte', convert_rgb_to_names(px))
        except NameError:
            print("Colornames could not be written due to unexpexted error. \n Der Pixel hat folgende Farbwerte: ", px)
    else:
        print('Erster Pixel zweite Spalte: ', img[0, 1])

    print('##############################################')


#def convert_rgb_to_names(rgb_tuple):
#    # a dictionary of all the hex and their respective names in css3
#    css3_db = css3_hex_to_names
#    names = []
#    rgb_values = []
#    for color_hex, color_name in css3_db.items():
#        names.append(color_name)
#        rgb_values.append(hex_to_rgb(color_hex))

#    kdt_db = KDTree(rgb_values)
#    distance, index = kdt_db.query(rgb_tuple)
#    return f'bestmögliche Farbbeschreibung: {names[index]}'

# Startet die Funktionen
def startUp(img):
    showImage(img)
    printImageDetails(img)
    myFirstImageManipulation(img)
    changeGrayscale(img)
    Utilities.showHistogram(img)
