from ImReader import ImReader
from LineDetector import LineDetector

if __name__ == "__main__":
    newImage = ImReader('E:/moje/kodziki/python/notesReader/Resources/notes2.jpg')
    newDetector = LineDetector(newImage)
    newDetector.showLinesImage()