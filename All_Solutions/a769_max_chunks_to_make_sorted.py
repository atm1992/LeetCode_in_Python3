# -*- coding: UTF-8 -*-
"""
title: 最多能完成排序的块
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].
We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.
Return the largest number of chunks we can make to sort the array.


Example 1:
Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


Constraints:
n == arr.length
1 <= n <= 10
0 <= arr[i] < n
All the elements of arr are unique.
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        """
        贪心
        由题意可知，arr中总共有n个元素，这些元素的范围为[0, n-1]，并且各个元素互不相同，所以对arr排序后，有 arr[i] = i
        因此，若arr的某个前缀块arr[0:i]的最大值等于下标i，则说明对该前缀块排序后与原数组排序后的结果一致。
        统计这些前缀块的数量，即可得到最终结果。
        """
        res = max_num = 0
        for i, num in enumerate(arr):
            max_num = max(max_num, num)
            if max_num == i:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().maxChunksToSorted([1, 0, 2, 3, 4]))
