import numpy as np
from linear_regression import LinearRegression, mean_squared_error, plot_regression

# Generate dummy dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Train model
model = LinearRegression(lr=0.01, epochs=1000)
model.fit(X, y)
predictions = model.predict(X)

print("Weights:", model.weights)
print("Bias:", model.bias)
print("MSE:", mean_squared_error(y, predictions))

# Plot results
plot_regression(X, y, predictions)
