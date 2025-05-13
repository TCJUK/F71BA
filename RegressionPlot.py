import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create synthetic data
np.random.seed(0)
x = 2.5 * np.random.randn(50) + 25    # 50 random x values around mean 25
y = 0.5 * x + np.random.randn(50) * 2 + 10  # y = 0.5*x + noise

# Reshape x to be a 2D array for sklearn
x_reshaped = x.reshape(-1, 1)

# Fit linear regression
model = LinearRegression()
model.fit(x_reshaped, y)
y_pred = model.predict(x_reshaped)

# Plotting
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Data points')
plt.plot(x, y_pred, color='red', linewidth=2, label='Regression line')
plt.title('Linear Regression Example')
plt.xlabel('X (e.g. Height)')
plt.ylabel('Y (e.g. Weight)')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('example-plot.png')
plt.show()