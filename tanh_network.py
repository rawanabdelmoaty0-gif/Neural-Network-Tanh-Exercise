import numpy as np

def tanh(x):
    return np.tanh(x)

x = np.array([0.5, -0.2])

# random weights in [-0.5, 0.5]
w1 = np.random.uniform(-0.5, 0.5, (2, 2))
w2 = np.random.uniform(-0.5, 0.5, (2, 1))


b1 = 0.5
b2 = 0.7

z1 = np.dot(x, w1) + b1
h = tanh(z1)

z2 = np.dot(h, w2) + b2
output = tanh(z2)

print("Network Output:", output)
