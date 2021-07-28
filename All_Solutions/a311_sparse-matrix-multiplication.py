# -*- coding: UTF-8 -*-
"""
title：稀疏矩阵的乘法。需要升级力扣 Plus 会员解锁题目
Example:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

输入两个二维数组，输出一个二维数组。稀疏矩阵的特点是矩阵中绝大多数的元素为0，要避免大量的重复计算0乘0
C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][k]*B[k][j]
只有当A[i][k]不为0时，才继续计算
"""


def sparse_matrix_multiplication(A, B):
    a_row = len(A)
    # A的列数就等于B的行数
    a_col = len(A[0])
    b_col = len(B[0])
    res = [[0] * b_col] * a_row
    for i in range(a_row):
        for j in range(a_col):
            if A[i][j] != 0:
                for k in range(b_col):
                    if B[j][k] != 0:
                        res[i][k] += A[i][j] * B[j][k]
    return res


if __name__ == '__main__':
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    print(sparse_matrix_multiplication(A, B))
