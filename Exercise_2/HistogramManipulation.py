import cv2
import numpy as np
import Utilities

# function to apply a look-up table onto an image
def applyLUT(img, LUT):
    result = img.copy()


    return result


# function to equalize a grayscale image
def equalizeHistogram(img):
    # result = img.copy()
    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    cdf = hist.cumsum()
    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')
    result = cdf[img]
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