import pandas as pd
import glob
import numpy as np

print("🔹 Step 1: Loading CSV files...")

files = glob.glob("MachineLearningCSV/*.csv")

df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)

print("Shape after merge:", df.shape)

print("🔹 Step 2: Cleaning data...")

df.columns = df.columns.str.strip()
df = df.replace([np.inf, -np.inf], np.nan)
df = df.dropna()

print("Shape after cleaning:", df.shape)

print("🔹 Step 3: Fixing labels...")

df["Label"] = df["Label"].str.strip()

df["Label"] = df["Label"].replace({
    "BENIGN": "Normal",
    "DoS Hulk": "DoS",
    "DoS GoldenEye": "DoS",
    "DoS slowloris": "DoS",
    "DoS Slowhttptest": "DoS",
    "Web Attack – Brute Force": "Web",
    "Web Attack – XSS": "Web",
    "Web Attack – Sql Injection": "Web"
})

print("🔹 Step 4: Saving cleaned dataset...")

df.to_csv("data/cicids_clean.csv", index=False)

print("✅ DONE! Dataset ready.")