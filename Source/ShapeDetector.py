import statistics
import numpy as np
import random
from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure
import skimage
from ImReader import *
from LineDetector import *
from skimage import measure
import cv2


class ShapeDetector:
    image = []
    contours = []
    centroids = []
    areas = []

    def __init__(self, image):
        self.image = image
        self.findContours()
        self.removeTrashes()

    def removeTrashes(self):
        for contour in self.contours:
            self.areas.append(cv2.contourArea(contour))

        for i in range(len(self.areas)):
            if self.areas[i] == max(self.areas):
                self.areas.pop(i)
                self.contours.pop(i)
                break

        median = statistics.median(self.areas)
        deviation = statistics.stdev(self.areas)
        toDelete = []

        for i in range(len(self.areas)):
            if self.areas[i] < median - 0.1 * deviation:
                toDelete.append(i)

            if self.areas[i] > median + 0.5 * deviation:
                toDelete.append(i)

        while len(toDelete) != 0:
            temp = toDelete.pop()
            self.areas.pop(temp)
            self.contours.pop(temp)

    def findContours(self):
        self.contours, hierarchy = cv2.findContours(self.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    def displayContours(self):
        fig, ax = plt.subplots()

        cv2.drawContours(self.image, self.contours, -1, (155, 255, 0), 2)

        ax.imshow(self.image)

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

    def findCentroid(self):
        for contour in self.contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                self.centroids.append((cX, cY))
                self.image[cY][cX] = 255


