# -*- coding: UTF-8 -*-
"""
title: 有序矩阵中第 K 小的元素
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
You must find a solution with a memory complexity better than O(n^2).


Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5


Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 300
-10^9 <= matrix[i][j] <= 10^9
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n^2

Follow up:
Could you solve the problem with a constant memory (i.e., O(1) memory complexity)?
Could you solve the problem in O(n) time complexity? The solution may be too advanced for an interview but you may find reading this paper fun.
"""
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        归并排序 + 最小堆。将原问题看作从n个有序子数组(n 行)中找出第k大的数，归并到第k个数时，即可停止
        一般归并排序是两个数组归并，而本题是 n 个数组归并，所以需要用小根堆维护，以优化时间复杂度
        """
        n = len(matrix)
        # 先将每行的第1个元素加入最小堆，并记录每个元素的坐标
        nums = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(nums)
        # 循环pop k-1 次，最后的nums[0][0]即为最终答案
        for i in range(k - 1):
            num, x, y = heapq.heappop(nums)
            if y < n - 1:
                # pop 了x行y列的元素后，补充x行y+1列的元素，始终保持nums中最多n个元素
                heapq.heappush(nums, (matrix[x][y + 1], x, y + 1))
        return nums[0][0]

    def kthSmallest_2(self, matrix: List[List[int]], k: int) -> int:
        """二分查找"""
        n = len(matrix)

        def check(mid: int) -> bool:
            """检查matrix中小于等于mid的元素个数是否大于等于k"""
            # 从左下角开始统计
            i, j = n - 1, 0
            cnt = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            return cnt >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) >> 1
            # 查找第一个满足cnt == k的值，因为1 <= k <= n^2，所以该值一定存在
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().kthSmallest(matrix=[[1, 5, 9], [10, 11, 13], [12, 13, 15]], k=8))
