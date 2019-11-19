import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

class LineDetector:
    image = []
    lines = []
    linesImage = []

    rhoAccuracy = 1
    thetaAccuracy = np.pi / 180
    treshold = 800
    linesColor = (0, 0, 255)

    def __init__(self, img):
        self.image = img
        self.lines = self.findLines()
        self.linesImage = self.drawLines(self.image.image)

    def findLines(self):
        return cv2.HoughLines(self.image.edges, self.rhoAccuracy, self.thetaAccuracy, self.treshold)

    def drawLines(self, img):
        linesImage = img
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

    def showLinesImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.linesImage)
        plt.show()