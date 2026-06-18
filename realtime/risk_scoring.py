import numpy as np

class RiskScorer:
    # Combines anomaly + classifier + behavior + temporal signals
    def normalize(self, x):
        return 1 - np.exp(-x)  # smooth scaling

    def compute(self, anomaly, confidence, behavior, temporal):
        anomaly = self.normalize(anomaly)

        # dynamic weighting
        if confidence < 0.5:
            w = [0.5, 0.2, 0.2, 0.1]
        else:
            w = [0.3, 0.4, 0.2, 0.1]

        risk = (
            w[0]*anomaly +
            w[1]*confidence +
            w[2]*behavior +
            w[3]*temporal
        )

        return float(np.clip(risk, 0, 1))

    def level(self, r):
        if r >= 0.8: return "HIGH"
        if r >= 0.5: return "MEDIUM"
        return "LOW"