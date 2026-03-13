import torch
import joblib
import pandas as pd
from models.autoencoder import Autoencoder

INPUT_DIM = 52

# Load trained autoencoder model
model = Autoencoder(INPUT_DIM)
model.load_state_dict(torch.load("models/saved/autoencoder.pth"))
model.eval()

# Load feature scaler used during training
scaler = joblib.load("models/saved/scaler.pkl")

# Threshold for anomaly detection
THRESHOLD = 0.01


def detect(features):

    # Convert feature list into DataFrame
    # so scaler receives correct feature names
    df = pd.DataFrame([features], columns=scaler.feature_names_in_)

    # Normalize features using saved scaler
    features = scaler.transform(df)[0]

    # Convert to PyTorch tensor
    x = torch.tensor(features).float().unsqueeze(0)

    # Perform model inference without gradient computation
    with torch.no_grad():
        output = model(x)

    # Compute reconstruction error
    loss = torch.mean((x - output) ** 2).item()

    # If error exceeds threshold → anomaly
    if loss > THRESHOLD:
        return "ANOMALY"

    return "NORMAL"