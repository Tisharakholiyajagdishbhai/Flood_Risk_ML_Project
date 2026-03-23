import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/flood_data.csv")

plt.scatter(data["rainfall"], data["river_level"], c=data["flood"])
plt.xlabel("Rainfall")
plt.ylabel("River Level")
plt.title("Flood Risk Visualization")

plt.savefig("results/flood_plot.png")
plt.show()
