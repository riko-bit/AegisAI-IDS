import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load the cleaned dataset produced during the preprocessing stage
df=pd.read_csv("data/processed/clean.csv")

# Separate features (network traffic attributes) from the label column
# X contains the input features used by the ML models
X=df.drop(columns=["Label"])

# y contains the target labels (Normal / Attack types)
y=df["Label"]

# StandardScaler is used to normalize the feature values
# This ensures all features have similar scale and improves model performance
scaler=StandardScaler()

# Fit the scaler on the dataset and transform the features
X_scaled=scaler.fit_transform(X)

# Save the fitted scaler so it can be reused during realtime inference
# This ensures realtime traffic is normalized in the same way as training data
joblib.dump(scaler,"models/saved/scaler.pkl")

print("Features processed")