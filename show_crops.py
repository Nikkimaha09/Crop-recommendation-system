import pandas as pd

df = pd.read_csv('Crop_recommendation.csv')
print(df['label'].unique())
print("Number of unique crops:", df['label'].nunique())