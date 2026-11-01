import numpy as np

x = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

w = np.array([0.0,0.0])
b = 0.0
lr = 0.1

for epoch in range(10):
    for i in range(4):
        net = np.dot(x[i],w) + b
        if net>=0:
            pred = 1
        else:
            pred = 0

        error = y[i] - pred
        w += error * lr * x[i]
        b += error * lr 

print("Trained Weights : ",w)
print("Bias : ",b)

for i in range(4):
    net = np.dot(x[i],w) + b
    if net>=0:
        pred = 1
    else:
        pred = 0

    print(f"Input: {x[i]}  ->  Predicted Output: {pred}")