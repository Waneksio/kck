from ImReader import *
from LineDetector import *
from ShapeDetector import *
from NotesRecognizer import *

if __name__ == "__main__":

    """NewImage = ImReader("../Resources/notes2.jpg")
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
    NewLineDetector.showNoLinesImage()"""

    NewImage = ImReader("../Resources/notes5.jpg")
    # NewImage.showBinImage()
    NewLineDetector = LineDetector(NewImage)
    # NewLineDetector.showNoLinesImage()
    cv2.imshow("image", NewLineDetector.noLinesImage)
    cv2.waitKey()
    NewDetector = ShapeDetector(NewLineDetector.noLinesImage)
    # cv2.imshow("image", NewDetector.image)
    # cv2.waitKey()
    newRecognizer = NotesRecognizer(NewLineDetector, NewDetector)
    print(newRecognizer.heights)
    for i in range(len(newRecognizer.imageLines)):
        print(newRecognizer.imageLines[i].b)
    # plt.figure(figsize=(10, 10))
    # io.imshow(NewDetector.image)
    # plt.show()

