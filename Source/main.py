from ImReader import *
from LineDetector import *
from ShapeDetector import *
from NotesRecognizer import *

if __name__ == "__main__":
    NewImage = ImReader("../Resources/easy/e1.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
    NewImage = ImReader("../Resources/easy/e2.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
    NewImage = ImReader("../Resources/easy/e3.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
    NewImage = ImReader("../Resources/easy/e4.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
    NewImage = ImReader("../Resources/easy/e5.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
    NewImage = ImReader("../Resources/easy/e6.jpg")
    NewDetector = LineDetector(NewImage)
    NewDetector.showRotatedImage()
