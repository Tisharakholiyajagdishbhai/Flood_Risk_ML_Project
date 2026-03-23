import pickle
import pandas as pd

# load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# sample input (same order as training data)
sample = pd.DataFrame(
    [[120, 5]],
    columns=["rainfall",  "river_level"]
)

prediction = model.predict(sample)

if prediction[0] == 1:
    print("⚠️ Flood Risk Detected")
else:
    print("✅ No Flood Risk")
