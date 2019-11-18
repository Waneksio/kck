import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import io

class LineDetector:
    image = []

    def __init__(self, img):
        self.image = img

    def detectLines(self):
        lines = cv2.HoughLines(self.image, 1, np.pi / 180, 200)
        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(self.image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    def showImage(self):
        plt.figure(figsize=(10, 10))
        io.imshow(self.image)
        plt.show()