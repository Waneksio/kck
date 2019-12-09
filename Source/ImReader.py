from matplotlib import pyplot as plt
from skimage import io
import numpy as np
import cv2


class ImReader:
    image = []
    binImage = []
    gray = []
    imgHeight = 0
    imgWidth = 0
    imgChannels = 0

    def __init__(self, imagePath):
        self.image = self.readImage(imagePath)
        self.gray = self.BGR2GRAY(self.image)
        self.binImage = self.GRAY2BIN(self.gray)
        self.binImageNegative = self.toNegative(self.binImage)
        self.imgHeight, self.imgWidth, self.imgChannels = self.image.shape

    def readImage(self, imagePath):
        return cv2.imread(imagePath)

    def BGR2GRAY(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def GRAY2BIN(self, img):
        binImage = img.copy()

        MIN = np.min(binImage)
        MAX = np.max(binImage)

        norm = (binImage - MIN) / (MAX - MIN)
        norm[norm[:,:] > 1] = 1
        norm[norm[:,:] < 0] = 0

        if(np.average(norm) < 0.8):
            perc = 12
            limit = np.percentile(norm, perc)
        else:
            limit = 0.8

        norm[norm[:,:] >= limit] = 255
        norm[norm[:,:] < limit] = 0

        binImage = np.uint8(norm)
        return binImage

    def BIN2EDGES(self, bImg):
        img = bImg.copy()
        return cv2.Canny(img, 50, 150, apertureSize=3)

    def toNegative(self, img):
        res = 255 - img
        return res

    def showImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.image)
        plt.show()

    def showGray(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.gray)
        plt.show()

    def showBinImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.binImage, cmap='gray')
        plt.show()


