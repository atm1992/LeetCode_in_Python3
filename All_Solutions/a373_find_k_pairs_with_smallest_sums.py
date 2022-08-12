# -*- coding: UTF-8 -*-
"""
title: 查找和最小的 K 对数字
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
Define a pair (u, v) which consists of one element from the first array and one element from the second array.
Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.


Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


Constraints:
1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4
"""
import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        优先队列
        最小数对的下标一定是(0, 0)，根据当前的最小下标(i, j)计算下一次加入优先队列的下标：(i + 1, j)、(i, j + 1)
        为避免重复加入下标，可先将nums1中的前k个下标加入队列：(0, 0)、(1, 0)、……、(k-1, 0)，
        之后每次从队列中取出元素(i, j)时，只增加nums2中的下标，即 (i, j + 1)
        可行性分析：
        1、第一个取出的毫无疑问是(0, 0)，此时需要加入(0, 1)、(1, 0)，但根据上面的分析，只加入 (0, 1)。由于初始化队列时，已加入了(1, 0)，所以没问题
        2、假设第二个取出的是(0, 1)，此时需要加入(0, 2)、(1, 1)，但根据上面的分析，只加入 (0, 2)。虽然(1, 1)没有入队，但是不影响最终结果，
        因为(1, 0)还在队列中，它一定会小于(1, 1)。当取出(1, 0)时，(1, 1)才会入队。
        """
        m, n = len(nums1), len(nums2)
        res = []
        queue = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, m))]
        # 最终结果可能没有k个
        while queue and len(res) < k:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            if j + 1 < n:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
        return res
