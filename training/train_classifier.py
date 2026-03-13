import pandas as pd
from models.classifier import IDSClassifier

print("Loading dataset...")

# Load CICIDS dataset
df = pd.read_csv("data/cicids2017_clean.csv")

# Remove extra whitespace in column names
df.columns = df.columns.str.strip()

# Remove rows where label is missing
df = df.dropna(subset=["Attack Type"])

# Separate features and labels
X = df.drop(columns=["Attack Type"])
y = df["Attack Type"]

print("Training samples:", len(X))

# Initialize IDS classifier
model = IDSClassifier()

# Train the Random Forest model
model.train(X, y)

# Save trained classifier model
model.save("models/saved/classifier.pkl")

print("Classifier trained successfully")