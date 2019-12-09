from ImReader import *
from LineDetector import *
from ShapeDetector import *
from NotesRecognizer import *

if __name__ == "__main__":
    path = "../Resources/easy/e8.jpg"
    NewImage = ImReader(path)
    NewDetector = LineDetector(NewImage)
    NewDetector.showLinesImage()
    NewDetector.showNoLinesImage()
    NewShapeDetector = ShapeDetector(NewDetector.noLinesImage)
    NewRecognizer = NotesRecognizer(NewDetector, NewShapeDetector)
    image = cv2.imread('notes_1.jpg')
    plt.figure(figsize=(10, 10))
    io.imshow(image, cmap='gray')
    plt.show()