import cv2
import numpy as np
import Utilities
from matplotlib import pyplot as plt


# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()

    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            result[i, j] = LUT[result[i, j]]

    return result


# function to equalize a grayscale image
def equalizeHistogram(img):
    result = img.copy()

    L = 256
    N = result.size
    LUT = np.arange(256)

    hist = cv2.calcHist([result], [0], None, [L], [0, L])
    integral = hist.cumsum()
    #print('integ: ', integral)

    for i in range(LUT.size):
            LUT[i] = ((L - 1) / N) * integral[LUT[i]]

    print("Histogram equalized")
    return applyLUT(result, LUT)


# function to stretch a grayscale image
def stretchHistogram(img):
    result = img.copy()

    min = np.min(result)
    max = np.max(result)
    L = 256
    LUT = np.arange(256)

    for i in range(LUT.size):
            LUT[i] = ((LUT[i] - min) / (max - min)) * (L - 1)

    print("Histogram stretched")
    return applyLUT(result, LUT)


# function to create a vector containing the histogram
def calculateHistogram(img, nrBins):

    histogram = np.zeros([nrBins], dtype=np.int)

    return histogram


def logImg(img):
    result = img.copy()

    LUT = np.arange(256)

    for i in range(LUT.size):
             LUT[i] = (255 / np.log(255)) * np.log(LUT[i] + 1)


    print("Histogram logarithmisch")
    return applyLUT(result, LUT)


def expoImg(img):
    result = img.copy()

    LUT = np.arange(256)

    for i in range(LUT.size):
            LUT[i] = (255 / np.exp(255/255)) * np.exp(LUT[i]/255 - 1)

    print("Histogram exponentiell")
    return applyLUT(result, LUT)


def invImg(img):
    result = img.copy()

    LUT = np.arange(256)

    for i in range(LUT.size):
            LUT[i] = 255 - LUT[i]

    print("Histogram inverse")
    return applyLUT(result, LUT)


def threshImg(img):
    result = img.copy()

    LUT = np.arange(256)

    for i in range(LUT.size):
            if LUT[i] > 128:
                LUT[i] = 255
            else: LUT[i] = 0

    print("Histogram threshold")
    return applyLUT(result, LUT)


def fillgaps(img, name):
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
    plt.savefig('./SampleData/Edited/' + name + '.jpg')
    plt.show()

    return result