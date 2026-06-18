from collections import deque
import numpy as np

class TemporalBuffer:
    # Stores recent traffic for sequence awareness
    def __init__(self, size=10):
        self.buffer = deque(maxlen=size)

    def add(self, features):
        self.buffer.append(features)

    def score(self):
        if len(self.buffer) < self.buffer.maxlen:
            return 0.0

        arr = np.array(self.buffer)
        return float(np.std(arr))  # variance = instability