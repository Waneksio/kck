from matplotlib import pyplot as plt
from skimage import data, io, filters, exposure


class ImReader:
    image = []

    def __init__(self, imagePath):
        self.image = self.readImage(imagePath)

    def readImage(self, imagePath):
        return io.imread(imagePath)

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