import numpy as np
from scipy.linalg import inv

A = np.array([[4, 7],
              [2, 6]])

A_inverse = inv(A)

identity_matrix = np.dot(A, A_inverse)
identity_matrix = np.round(identity_matrix, decimals=5)

print(f"Original Matrix:\n{A}\n")
print(f"Inverse Matrix:\n{A_inverse}\n")
print(f"A * A_inv (Should be Identity Matrix):\n{identity_matrix}\n")