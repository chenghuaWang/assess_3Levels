import numpy as np
import pandas as pd
from scipy import sparse
from scipy.sparse.linalg import cg
import cv2

WIN_NAME = 'Test show'


def jacobi(a, b, x, k):
    d_data = a.diagonal()
    d_inv_buffer = 1 / d_data
    d = sparse.diags(d_data, dtype=np.int)
    d_inv = sparse.diags(d_inv_buffer, dtype=np.float)
    del d_data
    del d_inv_buffer
    r = a - d
    for j in range(0, k + 1):
        # x = d_inv_buffer * (b - r * x)
        x = d_inv * (b - r * x)
    return x


if __name__ == '__main__':
    A_buffer = pd.read_csv('A.txt', sep=',', header=None, dtype=str, na_filter=False)
    B_buffer = pd.read_csv('B.txt', sep=',', header=None, dtype=str, na_filter=False)
    A_matrix = np.array(A_buffer).astype(int)
    print(A_matrix)
    del A_buffer
    B_matrix = np.array(B_buffer).astype(int)
    B_matrix = B_matrix[:, 2]
    del B_buffer
    A_row = A_matrix[:, 0] - 1
    A_col = A_matrix[:, 1] - 1
    A_data = A_matrix[:, 2]
    sA = sparse.coo_matrix((A_data, (A_row, A_col)), shape=(196608, 196608), dtype=np.int)
    del A_row
    del A_col
    del A_data
    # print(sA)
    x0 = np.ones(256 * 256 * 3, dtype=np.float)
    x0 = jacobi(sA, B_matrix, x0, 5)
    print(x0)
    # x0, info = cg(sA, B_matrix)
    # print(x0)
    x0 = x0.astype(int)
    img = np.zeros((256, 256, 3), dtype=np.uint8)
    for i in range(0, 256):
        for j in range(0, 256):
            img[i][j][2] = x0[i * 256 + j]
    for i in range(0, 256):
        for j in range(0, 256):
            img[i][j][1] = x0[256 * 256 + i * 256 + j]
    for i in range(0, 256):
        for j in range(0, 256):
            img[i][j][0] = x0[256 * 256 * 2 + i * 256 + j]
    print(x0)
    np.savetxt("D:\AI_ML\pythonProject\project3.0\\x.txt", x0, fmt='%d', delimiter=',')
    cv2.imwrite("D:\AI_ML\pythonProject\project3.0\\x.jpg", img)
