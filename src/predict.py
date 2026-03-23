import pickle
import pandas as pd

def load_model():
    with open("results/flood_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def predict_flood(rainfall, river_level):
    model = load_model()
    data = pd.DataFrame([[rainfall, river_level]],
                        columns=["rainfall", "river_level"])
    pred = model.predict(data)[0]
    return "Flood Risk Detected" if pred == 1 else "No Flood Risk"

if __name__ == "__main__":
    rainfall = float(input("Enter rainfall: "))
    river_level = float(input("Enter river level: "))
    print(predict_flood(rainfall, river_level))
