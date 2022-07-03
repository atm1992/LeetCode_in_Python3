# -*- coding: UTF-8 -*-
"""
title: 螺旋矩阵 IV
You are given two integers m and n, which represent the dimensions of a matrix.
You are also given the head of a linked list of integers.
Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.
Return the generated matrix.


Example 1:
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.

Example 2:
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


Constraints:
1 <= m, n <= 10^5
1 <= m * n <= 10^5
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """按层模拟。优于逐个模拟"""
        res = [[-1] * n for _ in range(m)]
        node = head
        top, bottom, left, right = 0, m - 1, 0, n - 1
        # The number of nodes in the list is in the range [1, m * n]
        while True:
            for i in range(left, right + 1):
                res[top][i] = node.val
                node = node.next
                if not node:
                    return res
            for i in range(top + 1, bottom + 1):
                res[i][right] = node.val
                node = node.next
                if not node:
                    return res
            for i in range(right - 1, left - 1, -1):
                res[bottom][i] = node.val
                node = node.next
                if not node:
                    return res
            for i in range(bottom - 1, top, -1):
                res[i][left] = node.val
                node = node.next
                if not node:
                    return res
            top, bottom, left, right = top + 1, bottom - 1, left + 1, right - 1

    def spiralMatrix_2(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        """逐个模拟"""
        res = [[-1] * n for _ in range(m)]
        node = head
        # 分别代表4个方向：向右(只加col)、向下(只加row)、向左(只减col)、向上(只减row)
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0
        i = j = 0
        while node:
            res[i][j] = node.val
            node = node.next
            next_i, next_j = i + directions[direction_idx][0], j + directions[direction_idx][1]
            # 0 <= Node.val
            if not (0 <= next_i < m) or not (0 <= next_j < n) or res[next_i][next_j] != -1:
                direction_idx = (direction_idx + 1) % 4
            i, j = i + directions[direction_idx][0], j + directions[direction_idx][1]
        return res


def bulid_linked_list(arr: List[int]) -> ListNode:
    dummy_head = ListNode(-1)
    pre = dummy_head
    for num in arr:
        pre.next = ListNode(num)
        pre = pre.next
    return dummy_head.next


if __name__ == '__main__':
    head = bulid_linked_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])
    print(Solution().spiralMatrix_2(m=3, n=5, head=head))
