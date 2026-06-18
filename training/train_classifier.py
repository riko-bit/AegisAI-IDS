import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from models.classifier import IDSClassifier
from training.evaluate import evaluate

print("🔹 Loading data...")

X = pd.read_csv("data/X.csv")
y = pd.read_csv("data/y.csv").values.ravel()

# 🔥 FIX 1: Reduce dataset size (VERY IMPORTANT)
print("Original size:", X.shape)

X_sample = X.sample(n=200000, random_state=42)  # 200k rows
y_sample = y[X_sample.index]

print("Sampled size:", X_sample.shape)

# 🔥 Load scaler
scaler = joblib.load("models/saved/scaler.pkl")
X_scaled = scaler.transform(X_sample)

# 🔥 Split data
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_sample, test_size=0.2, random_state=42
)

print("🔹 Training classifier...")

model = IDSClassifier()
model.train(X_train, y_train)

# Save model
model.save("models/saved/classifier.pkl")

print("🔹 Evaluating...")

y_pred = model.model.predict(X_test)

evaluate(y_test, y_pred)

print("✅ Classifier trained successfully")