from ImReader import *
from LineDetector import *
from ShapeDetector import *
from NotesRecognizer import *

if __name__ == "__main__":
    path = "../Resources/medium/m3.jpg"
    NewImage = ImReader(path)
    NewDetector = LineDetector(NewImage)
    NewDetector.showLinesImage()
    NewDetector.showNoLinesImage()
    NewShapeDetector = ShapeDetector(NewDetector.noLinesImage)
    NewRecognizer = NotesRecognizer(NewDetector, NewShapeDetector)