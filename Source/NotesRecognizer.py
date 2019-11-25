

class NotesRecognizer:
    image = []
    centroids = []
    checked = []

    def __init__(self, image, centroids):
        self.image = image
        self.centroids = centroids

    def recognizeNote(self):
        """"pole pole łyse pole, ale mam już plan!"""