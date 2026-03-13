import pandas as pd

# Path to the raw CICIDS2017 dataset
INPUT="data/raw/cicids2017.csv"

# Path where the cleaned dataset will be saved
OUTPUT="data/processed/clean.csv"

# Load the raw dataset into a pandas DataFrame
df=pd.read_csv(INPUT)

# Remove duplicate rows to avoid bias during model training
df=df.drop_duplicates()

# Replace infinite values (which sometimes occur in network statistics)
# with 0 so that ML models can process the data
df=df.replace([float("inf"),-float("inf")],0)

# Remove rows containing missing values
# This ensures the dataset is clean and usable for training
df=df.dropna()

# Save the cleaned dataset to a new CSV file
df.to_csv(OUTPUT,index=False)

# Confirmation message
print("Clean dataset saved")