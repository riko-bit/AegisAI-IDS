import numpy as np

class OnlineLearner:
    # stores new data for periodic retraining
    def __init__(self):
        self.buffer = []

    def add(self, x, label):
        self.buffer.append((x, label))

    def ready(self):
        return len(self.buffer) > 500

    def get(self):
        X = np.array([i[0] for i in self.buffer])
        y = np.array([i[1] for i in self.buffer])
        self.buffer = []
        return X, y