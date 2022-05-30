# -*- coding: UTF-8 -*-
"""
title: 使数组按非递减顺序排列
You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
Return the number of steps performed until nums becomes a non-decreasing array.


Example 1:
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.

Example 2:
Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.


Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        """
        单调栈。
        对于一个非严格单调递增的序列(该序列左侧存在一个大于它们最大值的元素)，例如：[9, 1, 2, 2, 3, 4, 1, 5] 中的 [1, 2, 2, 3, 4]，
        该序列中每个元素被移除的时间点都是递增地加1，因为该序列中的所有元素会在每次step中只移除最左边的那一个。
        继续以 [9, 1, 2, 2, 3, 4, 1, 5] 为例，5 会因为9被移除，但是移除5之前，我们需要知道5前方非严格单调递增序列被移除的最大时间点，
        然后在这个基础上递增地加1。
        在示例 [9, 1, 2, 2, 3, 4, 1, 5] 中，5前方的非严格单调递增序列有两个：[1, 2, 2, 3, 4]、[1]，长度越长的序列，所能坚持的step个数越多，
        所以最大时间点对应的序列是：[1, 2, 2, 3, 4]，5被移除的时间点为4被移除的时间点的基础上加1；
        在示例 [9, 1, 2, 2, 3, 4, 8, 5] 中，5前方的非严格单调递增序列只有一个：[]，5被移除的时间点为1，表示5在第一轮就会被移除。
        """
        res = 0
        # stack 是一个单调递减栈
        stack = []
        for num in nums:
            # tmp用于记录当前num前方非严格单调递增序列被移除的最大时间点。注意：虽然说是序列，但是这个序列的长度是有可能为0、或可能为1的，不要单纯地认为序列就是一长串。
            # num前方非严格单调递增序列长度为0，分为两种情况：1、num是nums中的第一个元素，此时stack为空，最终该num对应的tmp为0，表示该num永远不会被移除；
            # 2、num紧接着的上一个元素比num大，此时stack不为空，最终该num对应的tmp为1，表示该num在第一轮就会被移除。
            tmp = 0
            while stack and stack[-1][0] <= num:
                tmp = max(tmp, stack.pop()[1])
            # 情况一：若stack不为空，则说明前方存在比num大的元素，该num被移除的时间点为，该num前方非严格单调递增序列被移除的最大时间点，再递增地加1。
            # 情况二：若stack为空，则说明该num是当前遇到的最大元素，左侧不存在能够把它移除的元素，所以它永远不会被移除，即 tmp == 0。
            # 以 [9, 1, 2, 2, 3, 4, 1, 5] 为例来分析情况一，[1, 2, 2, 3, 4] 被移除的时间点分别为 [1, 2, 3, 4, 5]
            # 以 [1, 2, 2, 3, 4, 1, 5] 为例来分析情况二，[1, 2, 2, 3, 4] 被移除的时间点分别为 [0, 0, 0, 0, 0]
            tmp = tmp + 1 if stack else 0
            res = max(res, tmp)
            stack.append((num, tmp))
        return res


if __name__ == '__main__':
    print(Solution().totalSteps([9, 1, 2, 2, 3, 4, 1, 5]))
