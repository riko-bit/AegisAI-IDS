from sklearn.ensemble import RandomForestClassifier
import joblib

# This class implements a traditional Machine Learning classifier
# used for identifying specific attack types after anomaly detection
class IDSClassifier:

    def __init__(self):

        # Initialize a Random Forest classifier
        # Random Forest works well for tabular network traffic data
        self.model=RandomForestClassifier(
            n_estimators=200,   # number of decision trees in the forest
            max_depth=15        # maximum depth of each tree to avoid overfitting
        )

    # Train the classifier using labeled data
    def train(self,X,y):

        # X = network traffic features
        # y = corresponding attack labels
        self.model.fit(X,y)

    # Predict the attack type for new traffic samples
    def predict(self,X):

        return self.model.predict(X)

    # Save the trained model to disk for later use
    def save(self,path):

        joblib.dump(self.model,path)