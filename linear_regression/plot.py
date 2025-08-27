import matplotlib.pyplot as plt
import numpy as np

def plot_regression(X, y, y_pred):
    plt.scatter(X, y, color="blue", label="Actual Data")
    plt.plot(X, y_pred, color="red", label="Regression Line")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.legend()
    plt.show()

def plot_loss(loss_history):
    plt.plot(range(len(loss_history)), loss_history, color="purple")
    plt.xlabel("Epochs")
    plt.ylabel("Loss (MSE)")
    plt.title("Loss Curve")
    plt.show()
