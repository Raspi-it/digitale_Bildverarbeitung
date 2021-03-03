import cv2
import numpy as np
import Utilities

# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()


    return result

# function to equalize a grayscale image
def equalizeHistogram(img):
    result = img.copy()


    print("Histogram equalized")
    return result

# function to stretch a grayscale image
def stretchHistogram(img):
    result = img.copy()

    print("Histogram stretched")
    return result


# function to create a vector containing the histogram
def calculateHistogram(img, nrBins):

    histogram = np.zeros([nrBins], dtype=np.int)

    return histogram



