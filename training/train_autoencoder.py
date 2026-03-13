import torch
import pandas as pd
import numpy as np
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler
import joblib

# Import the autoencoder model architecture
from models.autoencoder import Autoencoder

print("Loading dataset...")

# Load the cleaned CICIDS2017 dataset
df = pd.read_csv("data/cicids2017_clean.csv")

# Remove rows where attack labels are missing
df = df.dropna(subset=["Attack Type"])

print("Filtering normal traffic...")

# Train the autoencoder ONLY on normal traffic
# Autoencoders learn normal patterns and detect anomalies later
df = df[df["Attack Type"] == "Normal Traffic"]

print("Filtered dataset shape:", df.shape)

# Separate features from the label column
X = df.drop(columns=["Attack Type"])

# Replace infinite values with NaN
X = X.replace([np.inf, -np.inf], np.nan)

# Fill missing values with 0
X = X.fillna(0)

print("Feature shape:", X.shape)

# Normalize features so all values are on a similar scale
# This improves neural network training stability
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Save the scaler so the same normalization can be applied
# later during realtime detection
joblib.dump(scaler, "models/saved/scaler.pkl")

print("Converting to tensor...")

# Convert feature data into PyTorch tensor format
X = torch.tensor(X, dtype=torch.float32)

# Create dataset object for PyTorch training
dataset = TensorDataset(X)

# DataLoader helps feed the model batches of data
loader = DataLoader(dataset, batch_size=128, shuffle=True)

print("Building autoencoder...")

# Initialize autoencoder model
# Input dimension = number of features
model = Autoencoder(X.shape[1])

# Mean Squared Error is used to measure reconstruction loss
criterion = torch.nn.MSELoss()

# Adam optimizer updates model weights during training
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

print("Training model...")

# Train the autoencoder for 20 epochs
for epoch in range(20):

    total_loss = 0

    # Iterate through batches of data
    for batch in loader:

        x = batch[0]

        # Model attempts to reconstruct the input
        output = model(x)

        # Calculate reconstruction error
        loss = criterion(output, x)

        # Reset gradients before backpropagation
        optimizer.zero_grad()

        # Compute gradients
        loss.backward()

        # Update model weights
        optimizer.step()

        total_loss += loss.item()

    # Print training progress
    print(f"Epoch {epoch+1}/20  Loss: {total_loss:.4f}")

print("Saving model...")

# Save trained model weights for later inference
torch.save(model.state_dict(), "models/saved/autoencoder.pth")

print("Training complete.")