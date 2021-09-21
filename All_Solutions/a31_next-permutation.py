# -*- coding: UTF-8 -*-
"""
title: 下一个排列
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
The replacement must be in place and use only constant extra memory.


Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Example 4:
Input: nums = [1]
Output: [1]


Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        从后往前遍历，找到第一个nums[i] > nums[i-1]，此时可确保i~n-1是降序。然后再次从后往前遍历i~n-1，找到第一个大于i-1的元素，然后交换。
        交换后，依旧可确保i~n-1是降序的，然后直接将i~n-1转为升序即可。
        """
        n = len(nums)
        smaller_idx = n - 1
        # 退出for循环时，若 smaller_idx 还是 n - 1，则表示整个原始的nums就是降序，也就是说 整个序列已经是最大值
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                smaller_idx = i - 1
                break
        for i in range(n - 1, smaller_idx, -1):
            if nums[i] > nums[smaller_idx]:
                nums[i], nums[smaller_idx] = nums[smaller_idx], nums[i]
                break
        left = 0 if smaller_idx == n - 1 else smaller_idx + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    print(nums)
