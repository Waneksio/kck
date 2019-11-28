from ImReader import *
from LineDetector import *
from ShapeDetector import *

if __name__ == "__main__":

    NewImage = ImReader("../Resources/notes2.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

    NewImage = ImReader("../Resources/notes3.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

    NewImage = ImReader("../Resources/notes4.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

    NewImage = ImReader("../Resources/notes5.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

    NewImage = ImReader("../Resources/notes6.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

    NewImage = ImReader("../Resources/notes7.jpg")
    NewLineDetector = LineDetector(NewImage)
    NewLineDetector.showNoLinesImage()

