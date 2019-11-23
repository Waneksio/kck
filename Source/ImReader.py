import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure
import skimage
from skimage import io
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
        self.edges = self.BGR2EDGES(self.image)
        self.imgHeight, self.imgWidth, self.imgChannels = self.image.shape
        self.binImage = self.gray
        self.binImageConvert()

    def binImageConvert(self):
        for i in range(len(self.binImage)):
            for j in range(len(self.binImage[i])):
                if self.binImage[i][j] > 177:
                    self.binImage[i][j] = 255
                else:
                    self.binImage[i][j] = 0

    def readImage(self, imagePath):
        return io.imread(imagePath)
        return cv2.imread(imagePath)

    def BGR2GRAY(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def BGR2EDGES(self, img):
        grayImg = self.BGR2GRAY(img)
        return cv2.Canny(grayImg, 50, 150, apertureSize=3)

    def getImage(self):
        return self.binImage

    def showImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.image)
        plt.show()

    def wbConvert(self):
        for pixelArray in self.image:
            for pixel in pixelArray:
                if pixel > 200:
                    pixel = 255
                else:
                    pixel = 0

    def showGray(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.gray)
        plt.show()


