from data_loader import load_data
from model import train_model, save_model

def main():
    X, y = load_data()      
    model = train_model(X, y)
    save_model(model)
print("Model saved successfully")
if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt


