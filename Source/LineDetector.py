import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage import morphology as mp

class LineDetector:
    image = []
    lines = []
    linesImage = []
    noLinesImage = []

    rhoAccuracy = 1
    thetaAccuracy = np.pi / 180
    threshold = 800
    linesColor = (0, 0, 255)

    def __init__(self, img):
        self.image = img
        self.lines = self.findLines()
        self.linesImage = self.drawLines(self.image.image)
        self.noLinesImage = self.removeLines(self.image.getBinImage())
        self.image = self.image.getBinImage

    def findLines(self):
        return cv2.HoughLines(self.image.edges, self.rhoAccuracy, self.thetaAccuracy, self.threshold)

    def drawLines(self, img):
        linesImage = img.copy()
        for l in self.lines:
            for rho, theta in l:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + self.image.imgWidth * (-b))
                y1 = int(y0 + self.image.imgHeight * (a))
                x2 = int(x0 - self.image.imgWidth * (-b))
                y2 = int(y0 - self.image.imgHeight * (a))

                cv2.line(linesImage, (x1, y1), (x2, y2), self.linesColor, 2)
        return linesImage

    def removeLines(self, img):
        noLinesImage = img.copy()
        for l in self.lines:
            for rho, theta in l:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + self.image.imgWidth * (-b))
                y1 = int(y0 + self.image.imgHeight * (a))
                x2 = int(x0 - self.image.imgWidth * (-b))
                y2 = int(y0 - self.image.imgHeight * (a))

                #cv2.line(noLinesImage, (x1, y1), (x2, y2), (255, 255, 255), 3)

        noLinesImage = mp.dilation(noLinesImage)
        noLinesImage = mp.dilation(noLinesImage)
        noLinesImage = mp.dilation(noLinesImage)
        noLinesImage = mp.dilation(noLinesImage)
        noLinesImage = mp.erosion(noLinesImage)
        return noLinesImage

    def dilatation(self, img):
        dilatationImage = img.copy()
        for i in range(0):
            dilatationImage = mp.erosion(dilatationImage)
        return dilatationImage

    def showLinesImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.linesImage)
        plt.show()

    def showNoLinesImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.noLinesImage)
        plt.show()

    def showNoLinesImageDilatation(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.dilatation(self.noLinesImage))
        plt.show()