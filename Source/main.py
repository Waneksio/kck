from ImReader import *
from LineDetector import *
from ShapeDetector import *

if __name__ == "__main__":
    NewImage = ImReader("../Resources/notes3.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewDetector = ShapeDetector(NewLineDetector.dilatation(NewLineDetector.noLinesImage))
    NewDetector.findCentroid()
    print(NewDetector.centroids)
    plt.figure(figsize=(10, 10))
    plt.imshow(NewDetector.image)
    plt.show()
