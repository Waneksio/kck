import statistics
import numpy as np

class NotesRecognizer:
    LineDetector = 0
    ShapeDetector = 0
    imageLines = []
    distances = []
    heights = []
    avgDist = 0
    heightsDict = {0: "F",
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
        self.LineDetector = LineDetector
        self.ShapeDetector = ShpaeDetector
        self.sortLines()
        self.avgDist = self.avgDistBetweenLines()
        self.recognizeNote()

    def avgDistBetweenLines(self):
        self.getDistances()
        avg = statistics.mean(self.distances)
        deviation = np.std(self.distances)
        for i in range(len(self.distances) - 1, 0, -1):
            if self.distances[i] < avg - deviation:
                self.imageLines.remove(self.imageLines[i])
        self.getDistances()
        return statistics.mean(self.distances)

    def getDistances(self):
        self.distances = []
        for i in range(1, len(self.imageLines)):
            self.distances.append(self.imageLines[i].b - self.imageLines[i - 1].b)

    def sortingKey(self, line):
        return line.b

    def sortLines(self):
        self.imageLines = self.LineDetector.lines.copy()
        self.imageLines.sort(key=self.sortingKey)


    def recognizeNote(self):
        for centroid in self.ShapeDetector.centroids:
            for i in range(len(self.imageLines)):
                if self.imageLines[i].valueOf(centroid[0]) + self.avgDist / 6 > centroid[1] > self.imageLines[i].valueOf(centroid[0]) - self.avgDist / 6:
                    self.heights.append((centroid[0], centroid[1], self.heightsDict[i * 2]))
                elif self.imageLines[i].valueOf(centroid[0]) - self.avgDist * 2 / 6 > centroid[1] > self.imageLines[i].valueOf(centroid[0]) - self.avgDist * 4 / 6:
                    self.heights.append((centroid[0], centroid[1], self.heightsDict[i * 2 - 1]))
                else:
                    continue