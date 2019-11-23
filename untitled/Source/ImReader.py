import numpy as np
from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure
import skimage


class ImReader:
    image = []

    def __init__(self, imagePath):
        self.image = self.readImage(imagePath)
        self.wbConvert()

    def readImage(self, imagePath):
        result = io.imread(imagePath)
        if len(result.shape) != 2:
            result = result[:, :, 2]
        return result

    def getImage(self):
        return self.image

    def showImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.image)
        plt.show()

    def wbConvert(self):
        for i in range(len(self.image)):
            for j in range(len(self.image[i])):
                if self.image[i][j] > 200:
                    self.image[i][j] = 255
                else:
                    self.image[i][j] = 0

