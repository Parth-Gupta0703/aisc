import numpy as np

A = np.array([1, 1, -1, -1])
weights = np.outer(A, A)
np.fill_diagonal(weights, 0)

noisy = np.array([1, 1, -1, 1])
state = noisy.copy()

for i in range(5):
    result = np.dot(weights, state)
    state = np.where(result >= 0, 1, -1)

print("Stored Pattern (Memory):", A)
print("Noisy Input Provided:   ", noisy)
print("Recovered Memory Output:", state)