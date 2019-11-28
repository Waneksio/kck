from ImReader import *
from LineDetector import *
from ShapeDetector import *

if __name__ == "__main__":
    NewImage = ImReader("../Resources/notes3.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewDetector = ShapeDetector(NewLineDetector.noLinesImage)
    NewDetector.findCentroid()
    NewDetector.displayContours()

