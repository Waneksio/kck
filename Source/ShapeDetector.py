import numpy as np
import random
from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure
import skimage
from .Source/ImReader import *
from skimage import measure
import cv2


class ShapeDetector:
    image = []
    contours = []
    centroids = []

    def __init__(self, image):
        self.image = image
        self.findContours()

    def findContours(self):
        self.contours, hierarchy = cv2.findContours(self.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    def displayContours(self):
        fig, ax = plt.subplots()
        ax.imshow(self.image)

        for n, contour in enumerate(self.contours):
            ax.plot(contour[:, 1], contour[:, 0])

        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()

    def findCentroid(self):
        for contour in self.contours:
            M = cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            self.centroids.append((cX, cY))
            self.image[cY][cX] = 0


if __name__ == "__main__":
    NewImage = ImReader("test.png")
    NewDetector = ShapeDetector(NewImage.getImage())
    NewDetector.findCentroid()
    print(NewDetector.centroids)
    plt.figure(figsize=(10, 10))
    plt.imshow(NewDetector.image)
    plt.show()