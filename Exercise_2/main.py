import cv2
import HistogramManipulation as HM
import Utilities

# Press the green button in the gutter to run the script.
# Task 1:
# implement a function that stretches a grayscale image
#
# Task 2
# implement a function that equalizes a grayscale image
#
# Small hint: use the functions in Utilities
# def plotHistogramVector(histogram) to im visualize the histogram vector

# Extra:
# 1. implement the following point operator functions on grayscale images:
#    logarithm, exponential function, inverse, threshold
# 2. implement a function to remove the gaps in the histogram of a
#    stretched/ equalized image
# make sure to prevent pixel overflows or negative pixel values

if __name__ == '__main__':
    img = cv2.imread("../../SampleData/classics/lena.png",0)
    stretchedImg = HM.stretchHistogram(img)
    equalizedImg = HM.equalizeHistogram(img)
    Utilities.showHistogram(img)
    Utilities.showHistogram(stretchedImg)
    Utilities.showHistogram(equalizedImg)


    cv2.imshow("Image", img)
    cv2.waitKey()
    cv2.imshow("Image", stretchedImg)
    cv2.waitKey()
    cv2.imshow("Image", equalizedImg)
    cv2.waitKey()