import numpy as np

X = np.array([1, -1, 1])
y = 1
lr = 1.0

weights = np.array([0.0, 0.0, 0.0])

delta = lr * X * y
new_weights = weights + delta

print("Initial Weights:", weights)
print("Weight Delta:   ", delta)
print("Updated Weights:", new_weights)