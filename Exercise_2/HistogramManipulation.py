import cv2
import numpy as np
import Utilities
from matplotlib import pyplot as plt

# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()


    return result


# function to equalize a grayscale image
def equalizeHistogram(img):
    result = img.copy()

    L = 256
    N = result.size

    hist = cv2.calcHist([result], [0], None, [L], [0, L])
    integral = hist.cumsum()
    #print('integ: ', integral)

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i, j] = ((L - 1) / N) * integral[result[i, j]]

    print("Histogram equalized")
    return result


# function to stretch a grayscale image
def stretchHistogram(img):
    result = img.copy()

    min = np.min(result)
    max = np.max(result)
    L = 256

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i, j] = ((result[i, j] - min) / (max - min)) * (L - 1)

    print("Histogram stretched")
    return result


# function to create a vector containing the histogram
def calculateHistogram(img, nrBins):

    histogram = np.zeros([nrBins], dtype=np.int)

    return histogram

def logImg(img):
    result = img.copy()

    for i in range(result.shape[1]):
         for j in range(result.shape[0]):
             result[i, j] = 46 * np.log(result[i, j] + 1)


    print("Histogram logged :)")
    return result

def expoImg(img):
    result = img.copy()

    for i in range(result.shape[1]):
        for j in range(result.shape[0]):
            result[i, j] = 2 * np.exp((result[i, j]/46) - 1)

    print("Histogram exposed :)")
    return result


def invImg(img):
    result = img.copy()

    for i in range(result.shape[1]):
        for j in range(result.shape[0]):
            result[i, j] = 255 - result[i, j]

    print("Histogram exposed :)")
    return result


def threshImg(img):
    result = img.copy()

    for i in range(result.shape[1]):
        for j in range(result.shape[0]):
            if result[i, j] > 128:
                result[i, j] = 255
            else: result[i, j] = 0

    print("Histogram exposed :)")
    return result

def fillgaps(img):
    result = img.copy()

    L = 256
    N = result.size

    hist = cv2.calcHist([result], [0], None, [L], [0, L])

    i=0
    while i <= 254:
        if hist[i] == 0:
            hist[i] = (hist[i - 1] + hist[i + 1])/2
        i = i + 1

    plt.close()
    plt.plot(hist, color='b')
    plt.xlim([0, 256])
    plt.show()

    return result