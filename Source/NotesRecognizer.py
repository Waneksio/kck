import statistics
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class NotesRecognizer:
    font = ImageFont.truetype('Roboto-Bold.ttf', size=26)
    LineDetector = 0
    ShapeDetector = 0
    imageLines = []
    staffs = []
    distances = []
    heights = []
    avgDist = 0
    heightsDict = {-1: "G",
                    0: "F",
                    1: "E",
                    2: "D",
                    3: "C",
                    4: "H",
                    5: "A",
                    6: "G",
                    7: "F",
                    8: "E",
                    9: "D"}

    def __init__(self, LineDetector, ShpaeDetector):
        image = Image.open("rotated.jpg")
        draw = ImageDraw.Draw(image)
        color = 'rgb(255, 0, 255)'
        self.LineDetector = LineDetector
        self.ShapeDetector = ShpaeDetector
        self.sortLines()
        for line in self.imageLines:
            print(line.b)
        self.avgDist = self.avgDistBetweenLines()
        self.recognizeNote(draw, color)
        image.save('notes_1.jpg')

    def avgDistBetweenLines(self):
        self.getDistances(self.imageLines)
        avg = statistics.mean(self.distances)
        deviation = np.std(self.distances)
        buffer = []
        for i in range(len(self.distances) - 1, -1, -1):
            if self.distances[i] < avg - 1 * deviation:
                self.imageLines.remove(self.imageLines[i + 1])
            else:
                buffer.insert(0, self.imageLines[i + 1])
                self.imageLines.remove(self.imageLines[i + 1])
            if self.distances[i] > avg + deviation:
                self.staffs.append(buffer)
                buffer = []
        buffer.insert(0, self.imageLines[0])
        self.imageLines.remove(self.imageLines[0])
        self.staffs.append(buffer)
        self.getDistances(self.staffs[0])
        return statistics.mean(self.distances)

    def getDistances(self, argList):
        self.distances = []
        for i in range(1, len(argList)):
            self.distances.append(argList[i].b - argList[i - 1].b)

    def sortingKey(self, line):
        return line.b

    def sortLines(self):
        self.imageLines = self.LineDetector.lines.copy()
        self.imageLines.sort(key=self.sortingKey)

    def recognizeNote(self, draw, color):
        for centroid in self.ShapeDetector.centroids:
            for staff in self.staffs:
                for i in range(len(staff)):
                    if staff[i].valueOf(centroid[0]) + self.avgDist / 3 > centroid[1] > staff[i].valueOf(centroid[0]) - self.avgDist / 3:
                        self.heights.append((centroid[0], centroid[1], self.heightsDict[i * 2]))
                        draw.text((centroid[0], centroid[1] - 20), self.heightsDict[i * 2], fill=color, font=self.font)
                    elif staff[i].valueOf(centroid[0]) - self.avgDist / 3 > centroid[1] > staff[i].valueOf(centroid[0]) - self.avgDist * 2 / 3:
                        self.heights.append((centroid[0], centroid[1], self.heightsDict[i * 2 - 1]))
                        draw.text((centroid[0], centroid[1] - 20), self.heightsDict[i * 2 - 1], fill=color, font=self.font)
                    else:
                        continue
    def printNotes(self):
        for height in self.heights:
            """do nothing"""
