from ImReader import ImReader
from LineDetector import LineDetector

if __name__ == "__main__":
    newImage = ImReader('E:/moje/kodziki/python/notesReader/Resources/notes.jpg')
    newImage.wbConvert()
    newDetector = LineDetector(newImage.image)
    newDetector.detectLines()
    newDetector.showImage()