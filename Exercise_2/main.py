import cv2
import HistogramManipulation as HM
import Utilities

# Fabian Mechelke, Mika Wiesemann, Elliott Engel, Maximilian Lindner

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
    # Bild laden und in Grauwertbild laden
    img = cv2.imread("./SampleData/classics/lena.png", 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Bild in mehreren Versionen bearbeiten lassen, sowie abspeichern
    stretchedImg = HM.stretchHistogram(img)
    cv2.imwrite('./SampleData/Edited/stretchedImage.jpg', stretchedImg)
    print('Image was saved.')

    equalizedImg = HM.equalizeHistogram(img)
    cv2.imwrite('./SampleData/Edited/equalizedImage.jpg', equalizedImg)
    print('Image was saved.')

    expImg = HM.expoImg(img)
    cv2.imwrite('./SampleData/Edited/exponentiellImage.jpg', expImg)
    print('Image was saved.')

    inverseImg = HM.invImg(img)
    cv2.imwrite('./SampleData/Edited/inverseImage.jpg', inverseImg)
    print('Image was saved.')

    threshImg = HM.threshImg(img)
    cv2.imwrite('./SampleData/Edited/thresholdImage.jpg', threshImg)
    print('Image was saved.')

    LogImg = HM.logImg(img)
    cv2.imwrite('./SampleData/Edited/logarithmischImage.jpg', LogImg)
    print('Image was saved.')

    # Histogramme erstellen und anzeigen lassen
    Utilities.showHistogram(img)
    Utilities.saveHist(img, 'normaleHist')

    Utilities.showHistogram(stretchedImg)
    Utilities.saveHist(stretchedImg, 'stretchedHist')

    Utilities.showHistogram(equalizedImg)
    Utilities.saveHist(equalizedImg, 'equalizeHist')

    Utilities.showHistogram(expImg)
    Utilities.saveHist(expImg, 'expHist')

    Utilities.showHistogram(inverseImg)
    Utilities.saveHist(inverseImg, 'inverseHist')

    Utilities.showHistogram(threshImg)
    Utilities.saveHist(threshImg, 'thresholdHist')

    Utilities.showHistogram(LogImg)
    Utilities.saveHist(LogImg, 'logarithmischHist')

    # Bilder anzeigen lassen
    cv2.imshow("Original Image", img)
    cv2.imshow("Stretched Image", stretchedImg)
    cv2.imshow("Equalized Image", equalizedImg)
    cv2.imshow("Expo Image", expImg)
    cv2.imshow("Inverse Image", inverseImg)
    cv2.imshow("Threshold Image", threshImg)
    cv2.imshow("Log Image", LogImg)
    cv2.waitKey()

    # Gaps in den Histogrammen ausfüllen und anzeigen lassen
    fill = HM.fillgaps(stretchedImg, 'Stretched_image-FilledGaps')

    fill = HM.fillgaps(equalizedImg, 'Equalized_image-FilledGaps')

    fill = HM.fillgaps(inverseImg, 'inversed_image-FilledGaps')

    fill = HM.fillgaps(expImg, 'exponentiell_image-FilledGaps')

    fill = HM.fillgaps(LogImg, 'logarithmisch_image-FilledGaps')