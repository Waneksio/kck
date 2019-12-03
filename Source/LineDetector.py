import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io
from skimage import morphology as mp
from Line import *


class LineDetector:
    imageReader = []
    lines = []
    linesImage = []
    noLinesImage = []

    rhoAccuracy = 0.5
    thetaAccuracy = np.pi / 360
    threshold = 350
    linesColor = (0, 0, 255)

    def __init__(self, imgR):
        self.imageReader = imgR
        self.lines = self.findLines()
        self.linesImage = self.drawLines(self.imageReader.image)
        self.noLinesImage = self.removeLines(self.imageReader.binImage)

    def findLines(self):
        lines = cv2.HoughLines(self.imageReader.binImage, self.rhoAccuracy, self.thetaAccuracy, self.threshold)
        lines = self.linesConvert(lines)
        return lines

    def linesConvert(self, lines):
        newLines = []
        for l in lines:
            for rho, theta in l:
                if(theta == 0):
                    a = self.imageReader.imgHeight
                    b = 0
                    x1 = int(rho)
                    y1 = 0
                    x2 = int(rho)
                    y2 = int(self.imageReader.imgHeight)
                elif (1.57 < theta < 1.5716):
                    a = 0
                    b = rho / np.sin(theta)
                    x1 = 0
                    y1 = int(b)
                    x2 = int(self.imageReader.imgWidth)
                    y2 = int((a * x2) + b)
                else:
                    a = -1 / np.tan(theta)
                    b = rho / np.sin(theta)
                    x1 = 0
                    y1 = int(b)
                    x2 = int(self.imageReader.imgWidth)
                    y2 = int((a * x2) + b)
                newLine = Line((x1, y1), (x2, y2), a, b)
                newLines.append(newLine)
        return newLines

    def drawLines(self, img):
        linesImage = img.copy()
        for line in self.lines:
            cv2.line(linesImage, line.p1, line.p2, self.linesColor, 2)
        return linesImage

    def removeLines(self, img):
        noLinesImage = img.copy()
        for line in self.lines:
            cv2.line(noLinesImage, line.p1, line.p2, (255, 255, 255), 3)
        noLinesImage = self.dilatation(noLinesImage)
        return noLinesImage

    def dilatation(self, img):
        dilatationImage = img.copy()
        for i in range(7):
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