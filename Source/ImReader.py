from matplotlib import pyplot as plt
from skimage import io
import cv2


class ImReader:
    image = []
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

    def readImage(self, imagePath):
        return cv2.imread(imagePath)

    def BGR2GRAY(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def BGR2EDGES(self, img):
        grayImg = self.BGR2GRAY(img)
        return cv2.Canny(grayImg, 50, 150, apertureSize=3)

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