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
    rotatedImage = []

    rhoAccuracy = 0.5
    thetaAccuracy = np.pi / 360
    threshold = 160
    linesColor = (0, 0, 255)
    angle = 0

    def __init__(self, imgR):
        self.imageReader = imgR
        self.lines = self.findLines()
        self.linesImage = self.drawLines(self.imageReader.image)
        self.noLinesImage = self.removeLines(self.imageReader.binImage)
        self.angle = self.findAngle()
        self.rotatedImage = self.rotate_bound(self.imageReader.image, self.angle)

    def findAngle(self):
        lines = cv2.HoughLines(self.imageReader.edges, self.rhoAccuracy, self.thetaAccuracy, self.threshold)
        angle = lines[0][0][1]
        angle = np.rad2deg(angle) - 90
        return -angle

    def findLines(self):
        lines = cv2.HoughLines(self.imageReader.edges, self.rhoAccuracy, self.thetaAccuracy, self.threshold)
        lines = self.linesConvert(lines)
        return lines

    def rotate_bound(self, img, angle):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = img.shape[:2]
        (cX, cY) = (w // 2, h // 2)

        # grab the rotation matrix (applying the negative of the
        # angle to rotate clockwise), then grab the sine and cosine
        # (i.e., the rotation components of the matrix)
        M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))

        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY

        # perform the actual rotation and return the image
        return cv2.warpAffine(img, M, (nW, nH))

    def linesConvert(self, lines):
        newLines = []
        newLinesRhos = []
        for l in lines:
            for rho, theta in l:

                flag = True
                for r in newLinesRhos:
                    # delete lines describing the same line
                    if(r - 2 <= rho <= r + 2):
                        flag = False
                    # delete lines describing with different angle
                    if(theta <= self.angle - 4 or self.angle + 4 <= theta):
                        flag = False
                if(flag == False):
                    break

                if(theta == 0):
                    a = 0
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
                newLinesRhos.append(rho)
        return newLines

    def drawLines(self, img):
        linesImage = img.copy()
        for line in self.lines:
            cv2.line(linesImage, line.p1, line.p2, self.linesColor, 2)
        return linesImage

    def removeLines(self, img):
        noLinesImage = img.copy()
        for line in self.lines:
            cv2.line(noLinesImage, line.p1, line.p2, (255, 255, 255), 5)
        noLinesImage = self.dilatation(noLinesImage)
        return noLinesImage

    def dilatation(self, img):
        dilatationImage = img.copy()
        for i in range(9):
            dilatationImage = mp.erosion(dilatationImage)
        for i in range(3):
            dilatationImage = mp.dilation(dilatationImage)
        return dilatationImage

    def showLinesImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.linesImage)
        plt.show()

    def showNoLinesImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.noLinesImage)
        plt.show()

    def showRotatedImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.rotatedImage)
        plt.show()