import pandas as pd

features = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Fwd Packet Length Max",
    "Fwd Packet Length Min",
    "Fwd Packet Length Mean",
    "Fwd Packet Length Std",
    "Bwd Packet Length Max",
    "Bwd Packet Length Min",
    "Bwd Packet Length Mean",
    "Bwd Packet Length Std",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Flow IAT Max",
    "Flow IAT Min",
    "Packet Length Mean",
    "Packet Length Std",
    "FIN Flag Count",
    "PSH Flag Count",
    "ACK Flag Count"
]

chunks = []

print("Reading in chunks...")

for chunk in pd.read_csv(
    "data/cicids_clean.csv",
    chunksize=100000,
    low_memory=False,
    on_bad_lines='skip'
):
    chunk.columns = chunk.columns.str.strip()

    chunk = chunk[features + ["Label"]]

    chunks.append(chunk)

df = pd.concat(chunks, ignore_index=True)

X = df[features]
y = df["Label"]

X.to_csv("data/X.csv", index=False)
y.to_csv("data/y.csv", index=False)

print("✅ Done:", X.shape)