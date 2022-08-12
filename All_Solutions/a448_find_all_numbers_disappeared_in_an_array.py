# -*- coding: UTF-8 -*-
"""
title: 找到所有数组中消失的数字
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Example 2:
Input: nums = [1,1]
Output: [2]


Constraints:
n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))

    def findDisappearedNumbers_2(self, nums: List[int]) -> List[int]:
        """原地修改。若n=6，数字6存在，则将下标为5的元素加n; 若数字1存在，则将下标为0的元素加n。
        之后若发现下标为idx的元素小于等于n，则说明数字idx+1不存在"""
        n = len(nums)
        for num in nums:
            # 注意：不能写成 num % n - 1
            # 例如：n = 6, num = 6, 则 num % n - 1 = -1，而(num - 1) % n = 5，我们需要修改的是下标为5的元素
            # 之所以需要将num对n取余，是因为可能在遍历到当前num之前，已经对num加过一次n
            idx = (num - 1) % n
            # 最多只加一次n
            if nums[idx] <= n:
                nums[idx] += n
        res = [i + 1 for i in range(n) if nums[i] <= n]
        # 恢复nums
        for i in range(n):
            nums[i] = (nums[i] - 1) % n + 1
        return res


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers_2(nums=[4, 3, 2, 7, 8, 2, 3, 1]))
