import pandas as pd

def load_data():
    data = pd.read_csv("data/flood_data.csv")

    print("Dataset columns:", data.columns)

    X = data[['rainfall', 'river_level']]
    y = data['flood']

    print("Training features:", X.columns)

    return X, y
