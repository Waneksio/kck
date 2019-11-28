import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage import morphology as mp

class LineDetector:
    imageReader = []
    lines = []
    linesImage = []
    noLinesImage = []

    rhoAccuracy = 1
    thetaAccuracy = np.pi / 180
    threshold = 800
    linesColor = (0, 0, 255)

    def __init__(self, imgR):
        self.imageReader = imgR
        self.lines = self.findLines()
        self.linesImage = self.drawLines(self.imageReader.image)
        self.noLinesImage = self.removeLines(self.imageReader.binImage)

    def findLines(self):
        return cv2.HoughLines(self.imageReader.edges, self.rhoAccuracy, self.thetaAccuracy, self.threshold)

    def drawLines(self, img):
        linesImage = img.copy()
        for l in self.lines:
            for rho, theta in l:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + self.imageReader.imgWidth * (-b))
                y1 = int(y0 + self.imageReader.imgHeight * (a))
                x2 = int(x0 - self.imageReader.imgWidth * (-b))
                y2 = int(y0 - self.imageReader.imgHeight * (a))

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
                x1 = int(x0 + self.imageReader.imgWidth * (-b))
                y1 = int(y0 + self.imageReader.imgHeight * (a))
                x2 = int(x0 - self.imageReader.imgWidth * (-b))
                y2 = int(y0 - self.imageReader.imgHeight * (a))

                cv2.line(noLinesImage, (x1, y1), (x2, y2), (255, 255, 255), 3)

        noLinesImage = self.dilatation(noLinesImage)
        return noLinesImage

    def dilatation(self, img):
        dilatationImage = img.copy()
        for i in range(4):
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