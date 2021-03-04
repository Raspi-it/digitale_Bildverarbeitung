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
    img = cv2.imread("./SampleData/classics/lena.png", 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    stretchedImg = HM.stretchHistogram(img)
    cv2.imwrite('./SampleData/Edited/stretchedImage.jpg', stretchedImg)
    print('Image was saved.')

    equalizedImg = HM.equalizeHistogram(img)
    cv2.imwrite('./SampleData/Edited/equalizedImage.jpg', equalizedImg)
    print('Image was saved.')

    expImg = HM.expoImg(img)
    cv2.imwrite('./SampleData/Edited/exponentiellImage.jpg', expImg)

    inverseImg = HM.invImg(img)
    cv2.imwrite('./SampleData/Edited/inverseImage.jpg', inverseImg)

    threshImg = HM.threshImg(img)
    cv2.imwrite('./SampleData/Edited/thresholdImage.jpg', threshImg)

    LogImg = HM.logImg(img)
    cv2.imwrite('./SampleData/Edited/logarithmischImage.jpg', LogImg)


    Utilities.showHistogram(img)
    Utilities.saveHist(img, 'normaleHist')

    Utilities.showHistogram(stretchedImg)
    Utilities.saveHist(stretchedImg, 'stretchedHist')

    Utilities.showHistogram(equalizedImg)
    Utilities.saveHist(equalizedImg, 'equalizeHist')

    Utilities.showHistogram(expImg)
    Utilities.saveHist(equalizedImg, 'expHist')

    Utilities.showHistogram(inverseImg)
    Utilities.saveHist(equalizedImg, 'inverseHist')

    Utilities.showHistogram(threshImg)
    Utilities.saveHist(equalizedImg, 'thresholdHist')

    Utilities.showHistogram(LogImg)
    Utilities.saveHist(equalizedImg, 'logarithmischHist')

    cv2.imshow("Original Image", img)
    cv2.imshow("Stretched Image", stretchedImg)
    cv2.imshow("Equalized Image", equalizedImg)
    cv2.imshow("Expo Image", expImg)
    cv2.imshow("Inverse Image", inverseImg)
    cv2.imshow("Threshold Image", threshImg)
    cv2.imshow("Log Image", LogImg)
    cv2.waitKey()

    
    fill = HM.fillgaps(stretchedImg)
    Utilities.saveHist(fill, 'Stretched_image-FilledGaps')

    fill = HM.fillgaps(equalizedImg)
    Utilities.saveHist(fill, 'Equalized_image-FilledGaps')