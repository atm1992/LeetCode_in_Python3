# -*- coding: UTF-8 -*-
"""
title: 矩形区域不超过 K 的最大数值和
Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
It is guaranteed that there will be a rectangle with a sum no larger than k.


Example 1:
Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).

Example 2:
Input: matrix = [[2,2,-1]], k = 3
Output: 3


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-10^5 <= k <= 10^5

Follow up: What if the number of rows is much larger than the number of columns?
对于行数远大于列数的情况，则可以枚举矩形区域的左右边界
"""
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """有序集合 + 二分查找"""
        from sortedcontainers import SortedList
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        # i 表示矩形区域的上边界，j 表示矩形区域的下边界
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for col in range(n):
                    # 上边界维持不变，下边界逐步下移的过程中，更新每一列(从上到下)的加和
                    total[col] += matrix[j][col]
                # 因为元素值可以为负数，所以前缀和序列不一定是升序的。因此才用有序列表来对前缀和进行排序
                # total_sorted中的初始值0 表示以第0列作为左边界的情况
                total_sorted = SortedList([0])
                right_sum = 0
                for v in total:
                    # 不断更新右边界的前缀和
                    right_sum += v
                    # 以当前列为矩形区域的右边界，total_set中的所有元素都可作为矩形区域的左边界，因为是在从左往右遍历列。
                    # 要想使左右边界前缀和之差尽量大，且不超过k，则需使left_sum尽可能小，且不低于right_sum - k
                    # 因此，可使用二分来查找大于等于right_sum - k的第一个元素

                    # 自己写的二分查找超时，通过38/39个测试用例
                    # left, right = 0, len(total_sorted) - 1
                    # while left < right:
                    #     mid = (left + right) // 2
                    #     if total_sorted[mid] >= right_sum - k:
                    #         right = mid
                    #     else:
                    #         left = mid + 1
                    # if total_sorted[left] >= right_sum - k:
                    #     res = max(res, right_sum - total_sorted[left])

                    # 官方答案
                    lb = total_sorted.bisect_left(right_sum - k)
                    if lb != len(total_sorted):
                        res = max(res, right_sum - total_sorted[lb])

                    total_sorted.add(right_sum)
        return res


if __name__ == '__main__':
    print(Solution().maxSumSubmatrix(matrix=[[2, 2, -1]], k=3))
