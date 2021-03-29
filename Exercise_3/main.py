import cv2
import ImageFiltering as IF
import Utilities
import numpy as np

if __name__ == '__main__':
    # load image and apply filters
    # choose some sort of border handling that keeps the size of the processed image

    # Bild laden und in Grauwertbild laden
    img = cv2.imread("./SampleData/classics/lena.png", 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Original Bild', img)

    maf = img.copy()
    IF.createMovingAverageKernel(maf, 5)
    cv2.imshow('Moving Average Filter Image', maf)
    cv2.imwrite('./SampleData/Edited/moving_average_filter_img.jpg', maf)
    Utilities.showHistogram(maf)
    Utilities.saveHist(maf, 'moving_average_hist')

    mf = img.copy()
    IF.applyMedianFilter(mf, 5)
    cv2.imshow('Median Filter Image', mf)
    cv2.imwrite('./SampleData/Edited/median_filter_img.jpg', mf)
    Utilities.showHistogram(mf)
    Utilities.saveHist(mf, 'median_filter_hist')

    gf = img.copy()
    IF.gaussian(gf, 5, 0.8)
    cv2.imshow('Gauss Filter Image', gf)
    cv2.imwrite('./SampleData/Edited/gauss_filter_img.jpg', gf)
    Utilities.showHistogram(gf)
    Utilities.saveHist(gf, 'gauss_filter_hist')

    x_kl = IF.createSobelXKernel()
    y_kl = IF.createSobelYKernel()


    img_x_s = img.copy()
    img_y_s = img.copy()

    IF.applyKernelInSpatialDomain(img_x_s, x_kl)
    IF.applyKernelInSpatialDomain(img_y_s, y_kl)


    cv2.imshow("Sobel X", img_x_s)
    cv2.imwrite("./SampleData/Edited/sobel_x.jpg", img_x_s)

    cv2.imshow("Sobel Y", img_y_s)
    cv2.imwrite("./SampleData/Edited/sobel_y.jpg", img_y_s)


    cv2.waitKey(0)