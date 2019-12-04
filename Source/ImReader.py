from matplotlib import pyplot as plt
from skimage import io
import numpy as np
import cv2


class ImReader:
    image = []
    binImage = []
    gray = []
    edges = []
    imgHeight = 0
    imgWidth = 0
    imgChannels = 0

    def __init__(self, imagePath):
        self.image = self.readImage(imagePath)
        self.gray = self.BGR2GRAY(self.image)
        self.binImage = self.GRAY2BIN(self.gray)
        self.edges = self.BIN2EDGES(self.binImage)
        self.imgHeight, self.imgWidth, self.imgChannels = self.image.shape

    def readImage(self, imagePath):
        return cv2.imread(imagePath)

    def BGR2GRAY(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def GRAY2BIN(self, img):
        binImage = img.copy()
        MIN = np.min(binImage)
        MAX = np.max(binImage)

        for i in range(len(binImage)):
            for j in range(len(binImage[i])):
                k = (binImage[i][j] - MIN) / (MAX - MIN)
                if k < 0.5:
                    binImage[i][j] = 255
                else:
                    binImage[i][j] = 0

        #binImage = np.uint8(binImage)
        return binImage

    def BIN2EDGES(self, bImg):
        img = bImg.copy()
        return cv2.Canny(img, 50, 150, apertureSize=3)

    def showImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.image)
        plt.show()

    def showGray(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.gray)
        plt.show()

    def showEdges(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.edges)
        plt.show()

    def showBinImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.binImage)
        plt.show()


