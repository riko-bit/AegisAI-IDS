import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import DataLoader, TensorDataset

from models.autoencoder import Autoencoder

print("🔹 Loading data...")

X = pd.read_csv("data/X.csv")
y = pd.read_csv("data/y.csv").values.ravel()

# 🔥 FIX 1: normalize labels
y = pd.Series(y).astype(str).str.strip()

print("Unique labels:", y.unique())

# 🔥 FIX 2: detect correct normal label
NORMAL_LABEL = "Normal"
if NORMAL_LABEL not in y.unique():
    NORMAL_LABEL = "BENIGN"

print("Using normal label:", NORMAL_LABEL)

# 🔥 FIX 3: filter safely
X = X[y == NORMAL_LABEL]

print("Training samples:", X.shape)

if len(X) == 0:
    raise ValueError("❌ No normal samples found! Check label names.")

# 🔥 Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(scaler, "models/saved/scaler.pkl")

# 🔥 FIX 4: Use batching (VERY IMPORTANT)
X_tensor = torch.tensor(X_scaled).float()
dataset = TensorDataset(X_tensor)
loader = DataLoader(dataset, batch_size=1024, shuffle=True)

# Model
model = Autoencoder(input_dim=X_tensor.shape[1])

optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

print("🔹 Training autoencoder...")

# 🔥 More epochs + batching
for epoch in range(10):
    total_loss = 0

    for batch in loader:
        x_batch = batch[0]

        optimizer.zero_grad()
        output = model(x_batch)

        loss = torch.mean((x_batch - output) ** 2)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch}, Loss: {total_loss / len(loader)}")

torch.save(model.state_dict(), "models/saved/autoencoder.pth")

print("✅ Autoencoder trained successfully")