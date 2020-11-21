import cv2
import numpy as np
import copy
import pandas as pd

A_buffer = pd.read_csv('A.txt', sep=',', header=None, dtype=str, na_filter=False)
B_buffer = pd.read_csv('B.txt', sep=',', header=None, dtype=str, na_filter=False)
A_in = np.array(A_buffer).astype(int)
B_in = np.array(B_buffer).astype(int)
A_matrix = np.zeros((196608, 196608), dtype=np.uint8)
B_matrix = np.zeros(196608, dtype=np.uint8)
print(A_in.shape)
print(B_in.shape)

if __name__ == '__main__':
    for i in range(0, 804528):
        A_matrix[A_in[i][0] - 1][A_in[i][1] - 1] = A_in[i][2]
    for i in range(0, 196608):
        B_matrix[i] = B_in[i][2]

