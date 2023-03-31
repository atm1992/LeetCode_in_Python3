# -*- coding: utf-8 -*-
# @date: 2023/3/31
# @author: liuquan
"""
title: 算术三元组的数目
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:
i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.


Example 1:
Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.

Example 2:
Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.


Constraints:
3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
"""
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        """哈希表 + 枚举"""
        res, nums_set = 0, set()
        for num in nums:
            if num - diff in nums_set and num - 2 * diff in nums_set:
                res += 1
            nums_set.add(num)
        return res

    def arithmeticTriplets_2(self, nums: List[int], diff: int) -> int:
        """三指针"""
        res, n = 0, len(nums)
        j, k = 1, 2
        for i in range(n - 2):
            j = max(j, i + 1)
            while j < n - 1 and nums[j] - nums[i] < diff:
                j += 1
            if j == n - 1:
                break
            if nums[j] - nums[i] > diff:
                continue
            k = max(k, j + 1)
            while k < n and nums[k] - nums[j] < diff:
                k += 1
            if k == n:
                break
            if nums[k] - nums[j] == diff:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().arithmeticTriplets_2(nums=[4, 5, 6, 7, 8, 9], diff=2))
