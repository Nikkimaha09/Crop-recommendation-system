import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('Crop_recommendation.csv')

# Features and target
X = df.drop('label', axis=1)
y = df['label']

# Label encoding for target
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Scaling
minmax_scaler = MinMaxScaler()
X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

std_scaler = StandardScaler()
X_train_scaled = std_scaler.fit_transform(X_train_minmax)
X_test_scaled = std_scaler.transform(X_test_minmax)

# Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)

# Save model and scalers
pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(std_scaler, open('standscaler.pkl', 'wb'))
pickle.dump(minmax_scaler, open('minmaxscaler.pkl', 'wb'))
pickle.dump(label_encoder, open('labelencoder.pkl', 'wb'))

print("Training complete. Files saved: model.pkl, standscaler.pkl, minmaxscaler.pkl, labelencoder.pkl")