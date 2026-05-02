import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# 🔷 Sample dataset (demo purpose)
data = {
    'packet_size': [100, 2000, 150, 3000, 120, 5000, 80, 4500],
    'protocol': [0, 0, 0, 1, 0, 1, 0, 0],
    'flag': [0, 1, 0, 1, 0, 1, 0, 1],
    'label': [0, 1, 0, 1, 0, 1, 0, 1]  # 0 = Normal, 1 = Attack
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features & Labels
X = df[['packet_size', 'protocol', 'flag']]
y = df['label']

# Train model
model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')

print("✅ Model trained successfully and saved as model.pkl")

