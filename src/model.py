from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print("Model Accuracy:", acc)
    cm = confusion_matrix(y_test, y_pred)
    print("confusion Matrix:\n", cm)
    import matplotlib.pyplot as plt
    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig("results/confusion_matrix.png")
    plt.close()
    return model


def save_model(model):
    with open("results/flood_model.pkl", "wb") as f:
        pickle.dump(model, f)
def save_model(model):
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

