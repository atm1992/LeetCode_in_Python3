# -*- coding: UTF-8 -*-
"""
title: 元素值大于变化阈值的子数组
You are given an integer array nums and an integer threshold.
Find any subarray of nums of length k such that every element in the subarray is greater than threshold / k.
Return the size of any such subarray. If there is no such subarray, return -1.
A subarray is a contiguous non-empty sequence of elements within an array.


Example 1:
Input: nums = [1,3,4,3,1], threshold = 6
Output: 3
Explanation: The subarray [3,4,3] has a size of 3, and every element is greater than 6 / 3 = 2.
Note that this is the only valid subarray.

Example 2:
Input: nums = [6,5,6,5,8], threshold = 7
Output: 1
Explanation: The subarray [8] has a size of 1, and 8 > 7 / 1 = 7. So 1 is returned.
Note that the subarray [6,5] has a size of 2, and every element is greater than 7 / 2 = 3.5.
Similarly, the subarrays [6,5,6], [6,5,6,5], [6,5,6,5,8] also satisfy the given conditions.
Therefore, 2, 3, 4, or 5 may also be returned.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i], threshold <= 10^9
"""
from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        """并查集"""
        n = len(nums)
        # 因为子数组是连续的，对于一个元素来说，它要么和上一个元素组成子数组，要么和下一个元素组成子数组。
        # 这里固定一个方向合并(向下一个元素合并，即 向右)，合并之前需要找到下一个元素所在子集的根节点，因为统一向右合并，
        # 所以根节点肯定是子集的右端点。这里的下标n就是一个哨兵，让nums中的最后一个元素(下标为n-1)也有下一个元素
        parent = list(range(n + 1))
        # 初始化，每个子集的长度均为1。计算过程中，获取子集的长度之前，需要先获取到子集的根节点root，子集的长度为size[root]
        size = [1] * (n + 1)

        def find(i: int) -> int:
            if i != parent[i]:
                parent[i] = find(parent[i])
            return parent[i]

        # 从大到小遍历nums，idx记录元素在原始数组中的下标
        for num, idx in sorted(zip(nums, range(n)), reverse=True):
            # 子数组的长度k越大，threshold / k 就越小，子数组中的元素就越容易满足 > threshold / k 的要求。
            # 因为是从大到小遍历nums，若下一个元素还没访问过，则size[idx+1]为默认值1；
            # 如果访问过下一个元素，则size[idx+1]至少为2，即 因为如果访问过的话，那么下一个元素就肯定已经连到了它的下一个元素上，所以它们的长度至少为2
            # 也就是说，已访问过的元素长度为size[j_root] - 1，子集根节点肯定没被访问过，因为如果被访问过，那它就不会是根节点了，它就会连到它的下一个元素上了
            # 因为是从大到小遍历nums，所有已访问过的元素都会大于等于当前num，所以也就只需判断 num 是否大于 threshold / k
            j_root = find(idx + 1)
            parent[idx] = j_root
            size[j_root] += size[idx]
            k = size[j_root] - 1
            if num > threshold / k:
                return k
        return -1

    def validSubarraySize_2(self, nums: List[int], threshold: int) -> int:
        """
        单调栈。推荐此方法
        枚举每个元素，假设它就是子数组中的最小值，然后用单调栈来计算以当前元素为最小值的子数组，它的左右边界可以到哪，
        然后得到该子数组的长度k，再判断当前元素是否大于threshold / k
        """
        n = len(nums)
        # left[i] 表示左侧(nums[i]向左侧扩散方向)第一个小于nums[i]的下标，若左侧所有元素都大于等于nums[i]，则为默认值-1
        left, stack = [-1] * n, []
        for idx, num in enumerate(nums):
            while stack and stack[-1][1] >= num:
                stack.pop()
            if stack:
                left[idx] = stack[-1][0]
            stack.append((idx, num))

        # right[i] 表示右侧(nums[i]向右侧扩散方向)第一个小于nums[i]的下标，若右侧所有元素都大于等于nums[i]，则为默认值n
        right, stack = [n] * n, []
        for idx in range(n - 1, -1, -1):
            num = nums[idx]
            while stack and stack[-1][1] >= num:
                stack.pop()
            if stack:
                right[idx] = stack[-1][0]
            stack.append((idx, num))

        for idx, num in enumerate(nums):
            k = right[idx] - left[idx] - 1
            if num > threshold / k:
                return k
        return -1
