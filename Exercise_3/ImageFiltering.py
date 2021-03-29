import numpy as np
import cv2


# apply median filter
def applyMedianFilter(img, kSize):

    # das img bekommt border, aber temp hat keinen -> img hat somit pixel mehr und temp muss die Pixel verarbeiten
    temp = img

    # Border von 1 wenn kernelsize von 3, median position
    b_Size = int(kSize / 2)
    m_pos = int(kSize / 2)

    img = cv2.copyMakeBorder(img,
                             top=b_Size,
                             bottom=b_Size,
                             left=b_Size,
                             right=b_Size,
                             borderType=cv2.BORDER_REFLECT_101)

    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):

            # wird befuellt und hinterher angewendet
            middle = []

            for x in range(kSize):
                for y in range(kSize):

                    # anhaengen der errechneten Werte an das Array
                    middle.append(img[i+x, j+y])

            # Sortierung aufsteigend im Array
            middle.sort()

            # array wird auf temp uebertragen
            temp[i, j] = middle[m_pos]

    img = temp

    return 0

# create a moving average kernel of arbitrary size
def createMovingAverageKernel(img, kSize):

    # das img bekommt border, aber temp hat keinen -> img hat somit pixel mehr und temp muss die Pixel verarbeiten
    temp = img

    # Border von 1 wenn kernelsize von 3
    b_Size = int(kSize / 2)

    img = cv2.copyMakeBorder(img,
                             top=b_Size,
                             bottom=b_Size,
                             left=b_Size,
                             right=b_Size,
                             borderType=cv2.BORDER_REFLECT_101)

    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):

            # muss bei neuer Iteration 0 werden
            avr = 0

            # damit Kernelsize nicht ignoriert wird und mehrere Averages angewendet werden können
            for x in range(kSize):
                for y in range(kSize):

                    avr = avr + img[i+x, j+y]

                # anwenden vom avr
                temp[i, j] = int(avr/(kSize*kSize))

    img = temp

    return 0


def gaussian(img, ksize, s_dev):

    # das img bekommt border, aber temp hat keinen -> img hat somit pixel mehr und temp muss die Pixel verarbeiten
    temp = img

    # Border von 1 wenn kernelsize von 3
    b_Size = int(ksize / 2)

    img = cv2.copyMakeBorder(img,
                             top=b_Size,
                             bottom=b_Size,
                             left=b_Size,
                             right=b_Size,
                             borderType=cv2.BORDER_REFLECT_101)

    g_kl = createGaussianKernel(ksize, s_dev)

    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):

            # muss bei neuer Iteration 0 werden
            g = 0

            for x in range(ksize):
                for y in range(ksize):

                    # berechnung von gauss formel ueber createGaussianKernel
                    g += img[i + x, j + y] * g_kl[x, y]

            # gauss wird auf temp und spaeter auf img uebertragen
            temp[i, j] = int(np.round(g))

    img = temp

    return 0


# create a gaussian kernel of arbitrary size
def createGaussianKernel(ksize, s_dev):

    norm = int(ksize/2)
    kl = np.empty([ksize, ksize])

    for i in range(ksize):
        for j in range(ksize):
            kl[i, j] = (1 / (2*np.pi*np.square(s_dev)))*np.exp(-0.5*((np.square(i-norm)+np.square(j-norm))/(np.square(s_dev))))

    print(kl)

    return kl


# create a kernel of size 3x3
def createSobelXKernel():

    kl = [[1, 0, -1], [2, 0, -2], [1, 0, -1]]
    kl = np.array(kl)

    return kl


# create a kernel of size 3x3
def createSobelYKernel():

    kl = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    kl = np.array(kl)

    return kl


def applyKernelInSpatialDomain(img, kl):

    # das img bekommt border, aber temp hat keinen -> img hat somit pixel mehr und temp muss die Pixel verarbeiten
    temp = img

    # harter 3er kernel ermoeglicht direkte Implementation von Border = 1
    img = cv2.copyMakeBorder(img,
                             top=1,
                             bottom=1,
                             left=1,
                             right=1,
                             borderType=cv2.BORDER_REFLECT_101)

    for i in range(temp.shape[0]):
        for j in range(temp.shape[1]):

            s = 0

            for x in range(3):
                for y in range(3):

                    #
                    s += img[i+x, j+y]*kl[2-x, 2-y]

            s = (s+255)/2

            # sobel wird auf temp und spaeter auf img uebertragen
            temp[i, j] = int(np.round(s))

    img = temp

    return 0


# Extra: create an integral image of the given image
def createIntegralImage(img):
    return 0


# Extra: apply the moving average filter by using an integral image
def applyMovingAverageFilterWithIntegralImage(img, kSize):
    return 0


# Extra:
def applyMovingAverageFilterWithSeperatedKernels(img, kSize):
    return 0