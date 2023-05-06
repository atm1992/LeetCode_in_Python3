# -*- coding: utf-8 -*-
# @date: 2023/5/6
# @author: liuquan
"""
title: 下一个更大元素 II
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.


Example 1:
Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number.
The second 1's next greater number needs to search circularly, which is also 2.

Example 2:
Input: nums = [1,2,3,4,3]
Output: [2,3,4,-1,4]


Constraints:
1 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """单调栈。反向遍历"""
        n = len(nums)
        res = [-1] * n
        stack = [nums[-1]]
        visited = set()
        i = n - 2
        while stack:
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()
            # 注意：由于nums[i]可能为-1，所以不能使用 res[i % n] == -1 来判断某个位置是否被处理过
            if stack and i % n not in visited:
                res[i % n] = stack[-1]
                visited.add(i % n)
            if i >= 0:
                stack.append(nums[i])
            i -= 1
        return res

    def nextGreaterElements_2(self, nums: List[int]) -> List[int]:
        """单调栈。正向遍历"""
        n = len(nums)
        res = [-1] * n
        # 注意：此时stack中保存的是元素下标
        stack = []
        # 相当于 nums[:] + nums[:-1]
        for i in range(2 * n - 1):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
            if not stack:
                break
        return res


if __name__ == '__main__':
    print(Solution().nextGreaterElements_2(nums=[1, 2, 3, 4, 3]))
