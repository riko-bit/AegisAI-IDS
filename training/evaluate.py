from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

# Function used to evaluate classifier performance
# It compares predicted labels with true labels
def evaluate(y_true,y_pred):

    # Accuracy → percentage of correct predictions
    print("Accuracy",accuracy_score(y_true,y_pred))

    # Precision → how many predicted attacks were actually attacks
    print("Precision",precision_score(y_true,y_pred,average="macro"))

    # Recall → how many real attacks were correctly detected
    print("Recall",recall_score(y_true,y_pred,average="macro"))

    # F1 Score → harmonic mean of precision and recall
    print("F1",f1_score(y_true,y_pred,average="macro"))