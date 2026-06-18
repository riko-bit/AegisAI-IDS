from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

class IDSClassifier:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=200,
            max_depth=15
        )

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        pred = self.model.predict(X)[0]

        # get confidence (probability of predicted class)
        prob = np.max(self.model.predict_proba(X))

        return pred, float(prob)

    def save(self, path):
        joblib.dump(self.model, path)