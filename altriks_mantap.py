import numpy as np
import os

def penjumlahan_matriks(A, B):
    try:
        # jika dimensi matriks sama
        if A.shape == B.shape:
            C = A + B

        # jika dimensi matriks tidak sama
        elif A.shape != B.shape:
            raise ValueError
        
    except ValueError:
        print("Dimensi matriks tidak sama")

    return C

def pengurangan_matriks(A, B):
    try:
        # jika dimensi matriks sama
        if A.shape == B.shape:
            C = A - B

        # jika dimensi matriks tidak sama
        elif A.shape != B.shape:
            raise ValueError
    
    except ValueError:
        print("Dimensi matriks tidak sama")

    return C

def perkalian_matriks(A, B):
    try:
        # jika jumlah kolom matriks A sama dengan jumlah baris matriks B
        if A.shape[1] == B.shape[0]:
            C = A.dot(B)

        # jika jumlah kolom matriks A tidak sama dengan jumlah baris matriks B
        elif A.shape[1] != B.shape[0]:
            raise ValueError
    
    except ValueError:
        print("Dimensi matriks tidak sama")

    return C

def perkalian_skalar(A, B):
    C = A * B

    return C

# penjumalahan matriks
os.system('cls')

print(f"PENJUMLAHAN MATRIKS".center(25, "="), "\n")

A = np.array([[5, 3, 6], [9, 7, 10], [11, 4, 3]])
B = np.array([[6, 9, 8], [3, 7, 12], [9, 3, 10]])
C = penjumlahan_matriks(A, B)

print(C)
input("Tekan 'Enter' untuk melanjutkan")

# pengurangan matriks
os.system('cls')

print(f"PENGURANGAN MATRIKS".center(25, "="), "\n")

P = np.array([[-6, 3], [5, 0]])
Q = np.array([[-1, 9], [5, 7]])
R = pengurangan_matriks(P, Q)

print(R)
input("Tekan 'Enter' untuk melanjutkan")

# perkalian matriks
os.system('cls')

print(f"PERKALIAN MATRIKS".center(25, "="), "\n")

X = np.array([[9, 2, -5]])
Y = np.array([[3, -5, 10]])
Z = perkalian_matriks(X, Y)

print(Z)
input("Tekan 'Enter' untuk melanjutkan")

# perkalian skalar
os.system('cls')

print(f"PERKALIAN SKALAR".center(25, "="), "\n")

M = np.array([[3, 1, 9], [2, 1, 4], [1, 4, 5]])
N = 5
O = perkalian_skalar(M, N)

print(O)